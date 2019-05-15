# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:01:45 2019

@author: Adaloglou
"""
import urllib.request
import tarfile
import numpy as np
import nibabel as nib
import scipy
import dipy
import dipy.io
import dipy.core.gradients
import dipy.segment.mask
import dipy.reconst.dti  # fractional_anisotropy, color_fa, TensorModel
import PIL.Image


def read_exam(list, path):
    """
    Extracting a tar.gz file from URL.
    """
    if len(list) == 4:
        for file in list:
            if 'dti.nii' in file:
                img_dti = nib.load(path + file)
            elif 't1.nii' in file:
                img_t1 = nib.load(path + file)
            elif 'bval' in file:
                f_bval = path + file
            elif 'bvec' in file:
                f_bvec = path + file

        bvals, bvecs = dipy.io.read_bvals_bvecs(f_bval, f_bvec)

        return img_t1, img_dti, bvals, bvecs
    else:
        return None


def extract_exam(URL, PATH):
    """
    Reading a tar.gz file from URL.
    """
    split_url_list = URL.split('.')
    if split_url_list[-1] != 'gz' or split_url_list[-2] != 'tar':
        print("Not a tar.gz file")
    else:
        try:
            response = urllib.request.urlopen(URL)
            exam_tar = tarfile.open(fileobj=response, mode="r|gz")
            exam_tar.extractall(PATH)
            list_names = exam_tar.getnames()
            exam_tar.close()

        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            print('URL link is working fine')
    return list_names[1:]


def calculate_fa(img, b_vals, b_vecs):
    """
    Calculates fractional anisotropy, and colored fractional anisotropy
    """
    data = img.get_data()
    gtab = dipy.core.gradients.gradient_table(b_vals, b_vecs)
    tenmodel = dipy.reconst.dti.TensorModel(gtab)
    maskdata, _ = dipy.segment.mask.median_otsu(data, 2, 1)
    tenfit = tenmodel.fit(maskdata)
    fr_anis = dipy.reconst.dti.fractional_anisotropy(tenfit.evals)
    fr_anis[np.isnan(fr_anis)] = 0  # replacing Not a number voxaels with 0
    fr_anis = np.clip(fr_anis, 0, 1)
    rgb_fr = dipy.reconst.dti.color_fa(fr_anis, tenfit.evecs)
    return rgb_fr


def transform_coordinate_space(t1, dti, img_fa):
    """
    Transfers coordinate space from fractional anisotropy to t1 using the affine matrix of dti
    """
    aff_t1 = t1.affine
    aff_t2 = dti.affine
    inv_af_2 = np.linalg.inv(aff_t2)
    list_channels = []

    out_shape = t1.get_data().shape
    rgb_shape = img_fa.shape

    T = inv_af_2.dot(aff_t1)  # desired transformation
    for j in range(rgb_shape[3]):
        transformed = scipy.ndimage.affine_transform(img_fa[...,j], T, output_shape=out_shape)
        list_channels.append(transformed)
    final_image = np.asarray(list_channels).transpose(1, 2, 3, 0)
    return final_image


def save_superimposed(im1, im2, name):
    """
    Super imposed via blending 2 pillow images and saves the result
    """
    im1 = im1.convert("RGBA")
    im2 = im2.convert("RGBA")

    blended = PIL.Image.blend(im1, im2, alpha=.7)
    blended.save(name, "PNG")


def generate_random_slices(t1, cfa):

    img_cfa_1 = cfa[..., 0]   # temporarily only 1st channel used
    # slices  img_cfa_1
    im1 = PIL.Image.fromarray(np.uint8(img_cfa_1[..., 140]))
    im2 = PIL.Image.fromarray(np.uint8(img_cfa_1[:, 140, :]))
    im3 = PIL.Image.fromarray(np.uint8(img_cfa_1[100, :, :]))

    # slices  img_t1
    im_t1 = t1.get_data()
    t1_1 = PIL.Image.fromarray(im_t1[..., 140])
    t1_2 = PIL.Image.fromarray(im_t1[:, 140, :])
    t1_3 = PIL.Image.fromarray(im_t1[100, :, :])

    save_superimposed(t1_1, im1, PATH+"axial.png")
    save_superimposed(t1_2, im2, PATH+"coronal.png")
    save_superimposed(t1_3, im3, PATH+"saggital.png")


URL = "https://s3.eu-central-1.amazonaws.com/advantis-public/exam.tar.gz"
PATH = "./data/"
list_names = extract_exam(URL,PATH)
#list_names = ['exam/dti.nii', 'exam/dti.bval', 'exam/t1.nii', 'exam/dti.bvec']
data_tuple = read_exam(list_names, PATH)

if data_tuple is None:
    print("ERROR")
else:
    img_t1, img_dti, bvals, bvecs = data_tuple
    rgb_fa = 255*calculate_fa(img_dti, bvals, bvecs)
    nib.save(nib.Nifti1Image(np.array( rgb_fa, 'uint8'), img_dti.affine), PATH+'tensor_rgb.nii')

    transformed_cfa = transform_coordinate_space(img_t1, img_dti, rgb_fa)

    nib.save(nib.Nifti1Image(np.array(transformed_cfa, 'uint8'), img_t1.affine),
             PATH+'cfa_transformed.nii')

    generate_random_slices(img_t1, transformed_cfa)
    print("DONE")
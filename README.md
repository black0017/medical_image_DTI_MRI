# Medical Image processing project DTI & T1-MRI

## Assignment Description
- After downloading, extracting and reading the nii, bval and bvec files:
  1) Calculate the coloured FA (fractional anisotropy) map of the exam using the
    dti files. Doing so is quite complex so it's recommended to use the
    `dipy.reconst.dti` module of the `dipy` python library.
  2) Transform the coordinate space of the coloured FA map onto the coordinate
    space of the T1 sequence using the information taken from the affine
    headers of the nifti files. In order to do this, you **MUST** use
    `scipy.ndimage.affine_transform`.
  3) Generate png images for the middle axial, coronal and sagittal slices,
    displaying the grayscale T1 sequence with the coloured FA map
    semi-transparently superimposed on top of it. In order to do this, you
    **MUST** use `PIL.Image`.


## Instructions
To reproduce the code:
1) open the terminal in the project directory
2) run the following command: `sudo docker build -t enviroment:latest .`
3) to make sure the docker image is created run: `docker images`
4) run in sudo mode: `docker run -it enviroment`
5) run the command: `python3 script.py`
6) results will be produced in the data folder

Note: for the generated png images: ‘x’ - sagittal, ‘y’ - coronal, ‘z’ - axial views.


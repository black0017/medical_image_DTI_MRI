Programming task for the position of backend software engineer in Advantis
==========================================================================

Create a web application written in Python:

- The web app can be written using Django, Flask, Pyramid or any other python
  web framework of your choice.

- The web app should display a form that contains a single text field and a
  submit button.

- The text field should accept urls for tarballs.

- After pressing the submit button, the web app should download and extract the
  tarball.

- The tarball should contain 4 files:
  - t1.nii
  - dti.nii
  - dti.bval
  - dti.bvec

- If the url is invalid, the download fails, the downloaded file is not a valid
  tarball or if it doesn't contain files as described above, it should return
  an appropriate error in the HTTP response to the user.

- After extracting and reading the nii, bval and bvec files, the web app
 should:
  - Calculate the coloured FA (fractional anisotropy) map of the exam using the
    dti files. Doing so is quite complex so it's recommended to use the
    `dipy.reconst.dti` module of the `dipy` python library.
  - Transform the coordinate space of the coloured FA map onto the coordinate
    space of the T1 sequence using the information taken from the affine
    headers of the nifti files. In order to do this, you **MUST** use
    `scipy.ndimage.affine_transform`.
  - Generate png images for the middle axial, coronal and sagittal slices,
    displaying the grayscale T1 sequence with the coloured FA map
    semi-transparently superimposed on top of it. In order to do this, you
    **MUST** use `PIL.Image`.

- The backend code **MUST NOT** require an X server to run.

- The code **MUST** follow PEP8 (the python coding style standard). PEP8
  compliance can be checked by several tools, my personal favorite being
  flake8.

- Submitted code **MUST** be in a private git repo. If hosted in github, add
  dimrozakis as a collaborator. If in bitbucket, then share it to htuttle
  instead. If on a private server, give me access using my public SSH key
  (preferred username is dr):
  ```
  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCdC7DfdBZmsEAO5AhOPFPEF5CCH9GeIKMAxAdd+jTdK8qeG20b/mJ7i+74jSJ2YRDGV4M6EffAfqfONlljhWFH5/6ALLjZ3n1T8n2AxoXUH5C7wmHUKaGSjRUjzPW5ITLWuTWCO8lXSb7I+wV/f1yPlKtdpMTGWqT0bn4//9QuQtFdKH9yZx1fZH5OHuMcgEmHPGUza85hpZIaqvHHZXW79z7PpMJy1TmqMcSFgUWY5CRz2P7vxiWNFsci5eoljQxTY760+8Zi3WzGN0KVBNYyUoTgwxq3jy74VIVGmSe+7/YFzIGOpFKC9VmL3FBpg/a6NKuiEio7bc46lgPNfotDdfWKTDKGUIhSjKFH1OI6ZYsvt5s6yB7OFKV8hLbDOJOZKLQJl4MUEGMbHsVJLlx/tXGp4A+19P43NslACH1xbnFE6FbxjNtOiLxHHGGJKT+I1Z/MDdDoG09Zbx2+B4hDGMQ2NZnvMPHkPBDgDF91j1r83XZxuiELo9VlrshZFMKHRN3oC/HZKpn190hsBeWu6s6D5h4eqQhlDpUVHOupYN9p3qACxhwGcoyK3CpSDkGU5X+Gn+tLnrwqzAUyltQ8yWKmz5L2Sksl5ZVHFb7i34R7NLa3anWYD8K0fZ2mZNPiIXmH9xsU69j0Ar4mHXXFMt1U10aF/u1M4ASYad1d4w== Dimitris Rozakis
  ```

- The repo **MUST** contain a `README.md` file explaining how to set up the
  environment and run the code.

- Some sample tarballs containing nii/bval/bvec files for dMRI exams:
  - https://s3.eu-central-1.amazonaws.com/advantis-public/exam.tar.gz

- Bonus points for tests and docker/docker-compose setup.


The only hard technical requirement is that the task is written using the
Python programming language. Any framework or library of your choice may be
used as long as it doesn't conflict with explicit requirements defined above.




‘x’ - sagittal, ‘y’ - coronal, ‘z’ - axial




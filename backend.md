Programming task for the position of backend software engineer
==========================================================================

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
  instead.

- The repo **MUST** contain a `README.md` file explaining how to set up the
  environment and run the code.

- Some sample tarballs containing nii/bval/bvec files for dMRI exams:
  - https://s3.eu-central-1.amazonaws.com/advantis-public/exam.tar.gz

- Bonus points for tests and docker/docker-compose setup.


The only hard technical requirement is that the task is written using the
Python programming language. Any framework or library of your choice may be
used as long as it doesn't conflict with explicit requirements defined above.




‘x’ - sagittal, ‘y’ - coronal, ‘z’ - axial




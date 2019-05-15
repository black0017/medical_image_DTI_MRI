To reproduce the code:
1) open the terminal in change directory to the project folder
2) run the following command: sudo docker build -t enviroment:latest .
3) to make sure the docker image is created run: docker images
4) run in sudo mode: docker run -it enviroment
5) run the command: python3 script.py
6) results will be produced in the data folder

Note: for the generated png images: ‘x’ - sagittal, ‘y’ - coronal, ‘z’ - axial views.


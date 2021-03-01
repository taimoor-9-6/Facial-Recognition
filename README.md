# Facial-Recognition
In this project we performed facial recognition using OpenCV.
Help was taken from: https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/ on how to perform facial recogntion on a raspberry pi and then the code was edited to work on a CPU. 
There are three parts of the code:
1) automation.py -> in this part the name of the folder is taken as an input and the output is a folder of that name containing 10/11 images.
2) dataset.py/enocde_faces.py -> the input of this file is the path of our images folder that was created by automation.py and the output is a pickle file
3) facial_recognition.py/pi_face_recognition.py -> this takes input the path of the pickle file and the name of the person and outputs if the person scanned on a live feed or an image is the same person compared to the pickle file

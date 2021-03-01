import cv2
import os
import time
import face_recognition
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import pickle
from imutils import paths
import shutil

#Give the name of the person
scale=60
knownEncodings = []
knownNames = []
name="Muhammad"
def makefoler():
    print(name)


    #Make a folder of that name

    os.mkdir(name)

    camera = cv2.VideoCapture(0)
    for i in range(10):
        time.sleep(2)
        return_value, image = camera.read()
        imageName="x"+ str(i) +".jpg"
        cv2.imwrite(os.path.join(name,imageName),image)        
    del(camera)
    return name


def pickl(name):
    for filename in os.listdir(name):
        image=cv2.imread(os.path.join(name,filename))
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        width=int(rgb.shape[1] * scale/100)
        height=int(rgb.shape[0] * scale/100)
        dim=(width,height)
        rgb = cv2.resize(rgb,dim,interpolation=cv2.INTER_AREA)
        
        boxes = face_recognition.face_locations(rgb,model='hog')

        encodings = face_recognition.face_encodings(rgb, boxes)
        print("1")
        for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(name)
                print("12")
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    outfile = open(name + ".pickle", "wb")
    pickle.dump(data,outfile)
    shutil.rmtree(name)
    outfile.close()    
    
while True:
    print("Enter 1 to build database and 0 to quit")
    x=input()
    if x=="1":
        makefoler()
        print("done")
        pickl(name)
    elif x=="0":
        break

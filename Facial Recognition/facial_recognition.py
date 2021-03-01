from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import cv2
import time

ITERATION_LIMIT=3  # TO TRY AND DETECT FACES FOR MORE FRAMES
name="Taimoor_1"
path='./Taimoor_1.pickle'


def checkface(name,path):
    
    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(path, "rb").read())
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    print("done")
    
    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
#     vs = VideoStream(src=0).start()
    # vs = VideoStream(usePiCamera=True).start()
    vs=cv2.VideoCapture(0)
    vs.set(3,640)
    vs.set(4,480)
    time.sleep(2.0)
    print(vs)
    matches=[]
    x=0
    truecount=0
    count=0

    while True:

        _,frame = vs.read()
        frame=cv2.flip(frame,1)
#         frame = cv2.imread("cam.jpg")
    
   #     frame = imutils.resize(frame, width=500) #800 worked fine as well

#         cv2.imshow('',frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('frame', frame)
        k=cv2.waitKey(30) & 0xff
        if k==27:
                break
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
            minNeighbors=3, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)
    
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []
        
        
        for encoding in encodings:

            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            #if(matches) : print(u'{} => {}'.format(doc.id, doc.to_dict()))

        if (matches==None):
                            print("No face found")
                            break
        cv2.imshow("frm",frame)        
        if x>ITERATION_LIMIT:
            break
        #fps.update()
        x+=1
    
    #time.sleep(2.0)
    #fps.stop()
    #end_time=time.time()
    #print(matches)    
    for number in matches:
                            print(matches)
                            count=count+1;
                            if matches[number]==True: truecount=truecount+1 
    
    if(truecount<(0.90*count)):
                                print("Failure: Access Denied")
                                #print(matches)
    elif(truecount>(0.90*count)):
                                print(matches)
                                print("Detection Successful: Access Granted")
                                #print("Accuracy=",(truecount/count)*100,"%")
                              
    else:
         print("No Face Detected")
    #print(end_time)
    #print(end_time-start_time)
    #t=fps.elapsed()
    #print(t)
    #print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    #print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    #print(names)
    x=0;
    # do a bit of cleanup
    cv2.destroyAllWindows()
    #vs.stop()


while True:
	print("Enter 1 to perform facial recognition and 0 to quit")
	x=input()	
	if x=="1":	
		face=checkface(name,path)
	elif x=="0":
		break


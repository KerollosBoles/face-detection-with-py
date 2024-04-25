import cv2
import face_recognition
import numpy as np
import tenserflow as tf
import os

imgBackground= cv2.imread("data/Resources/background.png")
#importing the mode images into a list
folderModePath= '/data/Resources/Modes'
modePathList=os.listdir(folderModePath)
imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))


cap= cv2.VideoCapture(0)
cap.set(3, 640) #the diminishes of image size
cap.set(4, 480)


while True:
    success, img= cap.read()
    #setting the position of the images to get in the background
    imgBackground[162:162 + 480, 55:55 + 640] = img 
    
    imgBackground[44:44 + 633, 800:800 + 414] = imgModeList[3] #and 3 are the data the we will put it in later of our 3 students 



    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)

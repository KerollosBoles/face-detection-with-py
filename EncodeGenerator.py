import cv2
import face_recognition
import pickle
import os
#Importing student images
folderPath= '/data/images'
PathList=os.listdir(folderPath)
print(PathList)
imgList=[]
studentsIDs=[]
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
   # print(path)
   # print(os.path.splitext(path)) #for removing (.jpg) form the Id of an image|| and if we put [0] then we get the exact value
    
    studentsIDs.append(os.path.splitext(path))
print(studentsIDs)
 

def findEncodingImages(imagesList)
    encodeList=[]
    for image in imagesList:
        img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        encode= face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
encodeListKnow= findEncodingImages(imgList)
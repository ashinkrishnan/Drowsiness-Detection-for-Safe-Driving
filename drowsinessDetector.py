# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:24:20 2021

@author: MYPC
"""

import cv2   #oprncv library
import dlib  #face detector library
from scipy.spatial import distance  #to find the euclidean distance of "eye" points

def calculate_EAR(eye):#fundtion to find <Eye Aspect Ratio>
    A = distance.euclidean(eye[1],eye[5])
    B = distance.euclidean(eye[2],eye[4])
    C = distance.euclidean(eye[0],eye[3])
    
    ear_aspect_ratio = (A+B)/(2.0*C)
    return ear_aspect_ratio

cap = cv2.VideoCapture(0) #input from cam

counter=0  #initialize blink counter 
EYE_AR_CONSEC_FRAMES = 15  #setting frame numbers(runs blink counter for 20[say] frame)

PATH= r"C:\Users\MYPC\Desktop\opencv_pk\shape_predictor\shape_predictor_68_face_landmarks.dat"
hog_face_detector = dlib.get_frontal_face_detector()  #obj for face detecting
dlib_facelandmark = dlib.shape_predictor(PATH) #obj for facelandmark

while True: #while cam is on(first arg is ture)
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #conv to gray
    
    faces = hog_face_detector(gray) #face recc. using dlib library
    
    for face in faces: #iteratign through detected faces
        face_landmarks = dlib_facelandmark(gray,face)
        
        leftEye=[] #empty list to store left eye co-ordinates
        rightEye=[] #empty list to store right eye co-ordinates
        
        for n in range(36,42): #Get the specific numbers from "68 face landmark"
            x=face_landmarks.part(n).x #ploting the x co ordinates
            y=face_landmarks.part(n).y #ploting the y co ordicates
            leftEye.append((x,y))#append to the list
            next_point = n+1
            if n==41:#to get the exact eye -shape
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)#drawing line
            
        for n in range(42,48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n==47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)
        
        left_EAR  = calculate_EAR(leftEye)
        right_EAR = calculate_EAR(rightEye)
            
        EAR = (left_EAR+right_EAR)/2
        EAR = round(EAR,2)
        
        
            
        if EAR <0.23:
            counter+=1
            if counter>=EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame,"DROWSINESS DETECTED",(20,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2q)
                cv2.putText(frame,"Are You Sleepy ?",(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                print("Drowsy")
                
        else:
            counter=0
            
            
                
        print(EAR)
        
    cv2.imshow("Are you sleepy",frame)
        
        
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
            
                
            
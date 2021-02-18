# Drowsiness-Detection-for-Safe-Driving

This is a real time computer vision project using OpenCV,dlib,and Python
The techniques used are

1. Facial landmark detection
2. Eye aspect ratio

from Facial landmark detection,we use eye feature and then apply Eye aspect ratio(EAR) using euclidean distace by scipy library,by EAR we can determine whether eyes are open or not.
which means that if EAR value is higher then eyes must be opened and vice versa.

for displaying alarm we will obseve the EAR for decided numberof frames and if EAR is low for that number of frames then alarm message will be shown.(on further modification we can sound notifications by importing "beepy" module of python).The frame rate should be adjusted by tiral and error method and real world convenience.

![](https://github.com/ashinkrishnan/Drowsiness-Detection-for-Safe-Driving/blob/main/Screenshot%202021-02-17%20114147.png)
![](https://github.com/ashinkrishnan/Drowsiness-Detection-for-Safe-Driving/blob/main/Screenshot%202021-02-17%20114243.png)

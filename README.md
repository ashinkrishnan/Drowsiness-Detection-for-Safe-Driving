# Drowsiness-Detection-for-Safe-Driving

This is a real time computer vision project using OpenCV,dlib,and Python
The techniques used are

1. Facial landmark detection
2. Eye aspect ratio

from Facial landmark detection,we use eye feature and then apply Eye aspect ratio(EAR) using euclidean distace by scipy library,by EAR we can determine whether eyes are open or not.
which means that if EAR value is higher then eyes must be opened and vice versa.

for displaying alarm,we will obseve the threshold EAR value for the given number of frames and if EAR is below the threshold for that given number of frames then alarm message will be shown.(on further modification: sound notifications by importing "beepy" module of python).The number of frames and threshold EAR should be adjusted by tiral and error method of real world convenience.

special acknowledgement: https://www.pyimagesearch.com/ 

![](https://github.com/ashinkrishnan/Drowsiness-Detection-for-Safe-Driving/blob/main/Screenshot%202021-02-17%20114147.png)
![](https://github.com/ashinkrishnan/Drowsiness-Detection-for-Safe-Driving/blob/main/Screenshot%202021-02-17%20114243.png)

#!/bin/env python
import numpy as np
import cv2

#img = cv2.imread("1.tif")
#cv2.namedWindow("Image")
#cv2.imshow("Image", img)
#cv2.imwrite("2.tif", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#create a black image
img = np.zeros((512,512,3), np.uint8)

#draw a diagnoal blue line with thickness of 5 px
cv2.line(img, (0,0),(260,260),(255,0,0),5)
#draw a rectangle 
cv2.rectangle(img, (256,256), (500,500),(0,255,0),3)
#draw a circle
cv2.circle(img, (120,120), 100, (0,0,255), -1)
#draw a ellipse
cv2.ellipse(img,(400,400),(100,50),0,0,360,(255,255,255),-1)
#draw polys
pts = np.array([[10,5],[30,5],[60,60],[80,80],[20,90]],np.int32)
cv2.polylines(img,[pts],True, (0,255,255))
#show character
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'TEST TXT',(350,50),font,1,(255,255,255),1,cv2.LINE_AA)

cv2.imwrite("line.png", img)

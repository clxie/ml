#!/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('1.png')
pts=[]
x=[]
y=[]
color=[]
for i in range(5,49,2):
	e1 = cv2.getTickCount()
	img1 = cv2.medianBlur(img1, i)
	e2 = cv2.getTickCount()
	time = (e2 - e1)/cv2.getTickFrequency()
	x.append(i)
	y.append(time)
	color.append(np.arctan2(i,time))
	print ('Freq:',i,time)

#plt.scatter(x,y,s=75,c=color,alpha=0.5),plt.title('Time')
plt.plot(x,y,'*'),plt.title('time')
plt.show()

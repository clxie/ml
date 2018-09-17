#!/bin/env python 

import cv2
import numpy as np
from matplotlib import pyplot as plt

def calcImgHist(img):
	hist = cv2.calcHist([img],[0],None,[256],[0.0,255.0])
	minVal,maxVal,minLoc,maxLoc=cv2.minMaxLoc(hist)
	histImg = np.zeros([256,256,3],np.uint8)
	hpt = int(0.9*256)

	for h in range(256):
		intensity = int(hist[h]*hpt/maxVal)
		cv2.line(histImg,(h,256),(h,256 - intensity), [255,0,0])
	return histImg

img = cv2.imread('1.png')
b,g,r = cv2.split(img)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
histB = calcImgHist(b)
histG = calcImgHist(g)
histR = calcImgHist(r)

#plt.subplot(231),plt.imshow(imgGray),plt.title('Gray')
#plt.subplot(232),plt.imshow(img),plt.title('src')
plt.subplot(131),plt.imshow(histB),plt.title('Blue')
plt.subplot(132),plt.imshow(histG),plt.title('Green')
plt.subplot(133),plt.imshow(histR),plt.title('Red')
plt.show()

#cv2.imwrite('blue.png',histB)
#cv2.imwrite('green.png',histG)
#cv2.imwrite('red.png',histR)

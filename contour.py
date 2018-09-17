#!/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('th2.jpg')
h,w,t = img.shape
print('img height, width, type:',h ,w ,t)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(imgGray, 100,255, cv2.THRESH_BINARY)
cv2.imwrite('th2_binary.jpg',binary)
print('threshold ret:', ret)
imgs, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print('find contour ret:', ret)
img[0:h,0:w,0:t] = 0
cv2.drawContours(img, contours, -1, (255,255,255), 3)

cv2.imwrite('contours.jpg', img)

contour = cv2.imread('contours.jpg')

source = cv2.imread('th2.jpg')

#dst = cv2.addWeighted(contour, 0.5, source, 0.5, 0.9, 0)
dst = cv2.add(contour,source)
plt.subplot(221),plt.imshow(source),plt.title('src')
plt.subplot(222),plt.imshow(dst),plt.title('weighted')
plt.subplot(223),plt.imshow(contour),plt.title('contour')
plt.subplot(224),plt.imshow(imgs),plt.title('img')
plt.show()

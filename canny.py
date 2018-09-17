#!/bin/env python

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('th2.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
[h,w,t] = img.shape
cv2.imwrite('th2_gray.jpg',imgGray)
imgGray = cv2.imread('th2_gray.jpg');
imgGray1 = cv2.imread('th2_gray.jpg');
imgGray2 = cv2.imread('th2_gray.jpg');
imgGray3 = cv2.imread('th2_gray.jpg');
print('img width:', w)
print('img height:', h)
print('img type:', t)
print('img shape:', imgGray.shape)
print('img size:', imgGray.size)
print('img dtype:', imgGray.dtype)


imgSobel = cv2.Sobel(imgGray1, cv2.CV_16S,1,1,ksize=3)
img1 = cv2.imread('th2_gray.jpg');
cv2.convertScaleAbs(imgSobel,img1)
cv2.imwrite('th2_sobel.jpg', img1)

imgSobely = cv2.Sobel(imgGray2, cv2.CV_16S,0,1,ksize=3)
img2 = cv2.imread('th2_gray.jpg');
cv2.convertScaleAbs(imgSobely,img2)

imgLaplacian = cv2.Laplacian(imgGray3, cv2.CV_16S, ksize=3)
img3 = cv2.imread('th2_gray.jpg');
cv2.convertScaleAbs(imgLaplacian,img3)
cv2.imwrite('th2_laplacian.jpg',img3)

imgedge = cv2.Canny(imgGray, 100, 200)
cv2.imwrite('th2_canny.jpg', imgedge)
imgEdge = cv2.imread('th2_canny.jpg');

plt.subplot(231), plt.imshow(img), plt.title('souce')
plt.subplot(232), plt.imshow(imgGray), plt.title('canny')
plt.subplot(233), plt.imshow(imgEdge), plt.title('canny')
plt.subplot(234), plt.imshow(img1), plt.title('sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(img2), plt.title('sobely'), plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(img3), plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.show()

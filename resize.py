#!/bin/env python

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

#img1 = Image.open('2.tif')
#img1gray = img1.convert('L')
#img1gray.save('th2_gray1.jpg')
#print(img1gray.mode, img1gray.size,img1gray.format)
#
#img2 = cv2.imread('2.tif')
#img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#cv2.imwrite('th2_gray2.jpg', img2gray)
#print(img2gray.dtype,img2gray.shape, img2gray.size,)

img3=Image.open('th2.jpg')
gray3 = img3.convert('L')
img4=cv2.imread('th2.jpg')
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
[w,h] = img3.size
print(gray3.getpixel((int(w/2),int(h/2))))
print(gray4[int(w/2),int(h/2)])

for row in range(h):
	for col in range(w):
#		#for i3,v3 in zip(gray3.getpixel((col,row)),gray4[row,col]):
		if gray3.getpixel((col,row)) != gray4[row,col]:
			print('img different')
		#	if i3 != v3:
#plt.subplot(221), plt.imshow(img1), plt.title('image')
#plt.subplot(222), plt.imshow(img1gray), plt.title('gray1')
#plt.subplot(223), plt.imshow(img2), plt.title('cv2')
#plt.subplot(224), plt.imshow(img2gray), plt.title('gray2')
#plt.show()

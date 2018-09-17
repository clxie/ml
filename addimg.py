#!/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

def imginfo(img):
	print("Image shape:",img.shape)
	print("Image size:",img.size)
	print("Image dtype:",img.dtype)

img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')

imginfo(img1)
imginfo(img2)

if img1.size == img2.size :
	dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
	plt.subplot(131),plt.imshow(img1),plt.title('1.png')
	plt.subplot(132),plt.imshow(img2),plt.title('2.png')
	plt.subplot(133),plt.imshow(dst),plt.title('dst.png')
	plt.show()
else :
	print("TWO IMAGE SIZE different")

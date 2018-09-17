#!/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')

rows,cols,channels = img2.shape

roi = img1[0:rows,0:cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst

plt.subplot(131),plt.imshow(img1),plt.title("1.png")
plt.subplot(132),plt.imshow(img2),plt.title("2.png")
plt.subplot(133),plt.imshow(img2gray),plt.title("img12gray")
plt.show()
cv2.imwrite('1_2.png',img1)
cv2.imwrite('2_mask.png',mask)

#!/bin/env python

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread("1.png")
print("image shape:",img.shape)
print("image size:",img.size)
print("image dtype:",img.dtype)

roiimg = np.zeros((500,500,3),np.uint8)
roiimg[0:500,0:500] = img[100:600,100:600]
cv2.imwrite("iroi.png", roiimg)
r,g,b=cv2.split(img)
cv2.imwrite("r.png",r)
cv2.imwrite("g.png",g)
cv2.imwrite("b.png",b)

src = cv2.imread("iroi.png")
blue = [255,0,0]
replicate = cv2.copyMakeBorder(src,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(src,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(src,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(src,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(src,10,10,10,10,cv2.BORDER_CONSTANT,value=blue)
plt.subplot(231),plt.imshow(src,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
plt.show()

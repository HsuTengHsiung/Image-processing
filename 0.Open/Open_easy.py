import cv2
import time
import warnings
import os
warnings.filterwarnings('ignore')

k=3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k,k))
img = cv2.imread('../WhyNot.jpg')
cv2.imwrite('./result/org.jpg',img)

img = cv2.imread('../WhyNot.jpg',0) #直接读为灰度图像
cv2.imwrite('./result/gray.jpg',img)

ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化

for i in range(1000):
    img= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)

cv2.imwrite('./result/Open.jpg',img)

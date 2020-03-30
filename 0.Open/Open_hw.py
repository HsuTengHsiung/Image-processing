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

org = (40, 80)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 3
fontcolor = 255 # BGR
thickness = 1 
lineType = 4

bottomLeftOrigin = 1
for i in range(4):
    for j in range(25):
        img= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    text = 'Number:' + str( (i+1)*25 )
    img2 =img
    cv2.putText(img2, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
    cv2.imwrite( str(i)+'.jpg',img2)


cv2.imwrite('./result/Open.jpg',img)

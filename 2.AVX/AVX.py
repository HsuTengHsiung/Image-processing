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
print('AVX加速',cv2.useOptimized())
start = time.clock()
for i in range(10000):
        img= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
end = time.clock()
time1 = end-start
print('開啟AVX加速CLOSE運算10000次:',time1,'秒')


cv2.setUseOptimized(False)
print('\r\n')
print('AVX加速',cv2.useOptimized())
start = time.clock()
for i in range(10000):
        img= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
end = time.clock()
time2 = end-start
print('關閉AVX加速CLOSE運算10000次:',time2,'秒')
print('\r\n共加速',time2/time1,'倍')

cv2.imwrite('./result/Open.jpg',img)

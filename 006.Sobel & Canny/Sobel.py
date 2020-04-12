import cv2 
import numpy as np 

# =============================================================================
# img = cv2.imread('../098.picture/People.jpg', cv2.IMREAD_UNCHANGED)
# =============================================================================
img = cv2.imread('../098.picture/People.jpg',0)
#ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化

cv2.imshow('img', img)

x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
z = cv2.Sobel(img,cv2.CV_16S,1,1,ksize = 5)  #0,1,2 XY方向參數

absX = cv2.convertScaleAbs(x)   # 轉回uint8
absY = cv2.convertScaleAbs(y)
absZ = cv2.convertScaleAbs(z)
dst = cv2.addWeighted(absX,1,absY,1,0)
cv2.imshow("absX", absX)
cv2.imshow("absY", absY)
cv2.imshow("Result", dst)
cv2.imshow("Result_2", absZ)
 
cv2.waitKey(0) 
cv2.destroyAllWindows()

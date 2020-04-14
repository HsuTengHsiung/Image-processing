import cv2 
import numpy as np 

# =============================================================================
# img = cv2.imread('../098.picture/People.jpg', cv2.IMREAD_UNCHANGED)
# =============================================================================
img = cv2.imread('../098.picture/People.jpg',0)
#ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化

cv2.imshow('img', img)
cv2.imwrite('./Sobel_FurtherTest/Kernel_test/' + 'gray' +'.jpg',img)


img_HE =cv2.equalizeHist(img)
cv2.imshow('img_HE_Open', img_HE)
cv2.imwrite('./Sobel_FurtherTest/Kernel_HE_test/' + 'gray' +'.jpg',img_HE)

for i in range(0,10):
    z = cv2.Sobel(img,cv2.CV_16S,1,1,ksize = i*2+1)  #0,1,2 XY方向參數 ksize 1 3 5 7 9
    absZ = cv2.convertScaleAbs(z)
    cv2.imshow("kernel_size="+str(i*2+1), absZ)
    cv2.imwrite('./Sobel_FurtherTest/Kernel_test/' + str(i) +'.jpg',absZ)

for i in range(0,10):
    z = cv2.Sobel(img_HE,cv2.CV_16S,1,1,ksize = i*2+1)  #0,1,2 XY方向參數 ksize 1 3 5 7 9
    absZ = cv2.convertScaleAbs(z)
    cv2.imshow("kernel_size="+str(i*2+1), absZ)
    cv2.imwrite('./Sobel_FurtherTest/Kernel_HE_test/' + str(i) +'.jpg',absZ)

cv2.waitKey(0) 
cv2.destroyAllWindows()

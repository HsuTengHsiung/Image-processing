import cv2 
import numpy as np 

# =============================================================================
# img = cv2.imread('../098.picture/People.jpg', cv2.IMREAD_UNCHANGED)
# =============================================================================
img = cv2.imread('../098.picture/People.jpg',0)

cv2.imshow('img', img)

img_HE =cv2.equalizeHist(img)
cv2.imshow('img_HE', img_HE)
img_HE=img.copy()
# =============================================================================
# ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#二值化
# cv2.imshow('img_THRESH', img)
# print(ret)
# =============================================================================

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# =============================================================================
# img= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
# =============================================================================
img= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('img_Open', img)

img_HE= cv2.morphologyEx(img_HE, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('img_HE_Open', img_HE)
#==============================================================================


Sobel_X = cv2.Sobel(img,cv2.CV_16S,1,0,ksize = 3)  #0,1,2 XY方向參數
Sobel_X = cv2.convertScaleAbs(Sobel_X)
cv2.imshow("Result_X", Sobel_X)

Sobel_HE_X = cv2.Sobel(img_HE,cv2.CV_16S,1,0,ksize = 3)  #0,1,2 XY方向參數
Sobel_HE_X = cv2.convertScaleAbs(Sobel_HE_X)
cv2.imshow("Result_HE_X", Sobel_HE_X)

Sobel_Y = cv2.Sobel(img,cv2.CV_16S,0,1,ksize = 3)  #0,1,2 XY方向參數
Sobel_Y = cv2.convertScaleAbs(Sobel_Y)
cv2.imshow("Result_Y", Sobel_Y)

Sobel_HE_Y = cv2.Sobel(img_HE,cv2.CV_16S,0,1,ksize = 3)  #0,1,2 XY方向參數
Sobel_HE_Y = cv2.convertScaleAbs(Sobel_HE_Y)
cv2.imshow("Result_HE_Y", Sobel_HE_Y)

dst = cv2.addWeighted(Sobel_HE_X,0.5,Sobel_HE_Y,0.5,0)
#ret,dst = cv2.threshold(dst,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#二值化
cv2.imshow("HE_final", dst)

dst_normal = cv2.addWeighted(Sobel_X,0.5,Sobel_Y,0.5,0)
#ret,dst_normal = cv2.threshold(dst_normal,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#二值化
cv2.imshow("normal_Final", dst_normal)
cv2.imwrite('./Sobel_FurtherTest/final/' + 'dst_normal' +'.jpg',dst_normal)
ret,dst_normal = cv2.threshold(dst_normal,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#二值化
cv2.imwrite('./Sobel_FurtherTest/final/' + 'dst_normal_threshold' +'.jpg',dst_normal)


dst_open= cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel, iterations=1)
# =============================================================================
# dst_open= cv2.morphologyEx(dst_open, cv2.MORPH_CLOSE, kernel, iterations=1)
# =============================================================================
cv2.imshow('dst_open', dst_open)

dst_Close= cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel, iterations=1)
# =============================================================================
# dst_Close= cv2.morphologyEx(dst_Close, cv2.MORPH_OPEN, kernel, iterations=1)
# =============================================================================
cv2.imshow('dst_Close', dst_Close)

Final = cv2.addWeighted(dst,0.5,img_HE,0.5,0)
cv2.imshow("Final", Final)


cv2.waitKey(0) 
cv2.destroyAllWindows()

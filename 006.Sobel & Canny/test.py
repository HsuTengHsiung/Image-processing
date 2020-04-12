import cv2 
import numpy as np 

# =============================================================================
# img = cv2.imread('../098.picture/People.jpg', cv2.IMREAD_UNCHANGED)
# =============================================================================
img = cv2.imread('../098.picture/People.jpg',0)

cv2.imshow('img', img)

# =============================================================================
# ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#二值化
# cv2.imshow('img_THRESH', img)
# print(ret)
# =============================================================================

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,11))
CLOSE= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('img_CLOSE', CLOSE)

OPEN= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
cv2.imshow('img_OPEN', OPEN)

CLOSE_OPEN= cv2.morphologyEx(CLOSE, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('img_CLOSE_OPEN', CLOSE_OPEN)

OPEN_CLOSE= cv2.morphologyEx(OPEN, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('img_OPEN_CLOSEN', OPEN_CLOSE)

cv2.waitKey(0) 
cv2.destroyAllWindows()

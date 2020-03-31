import cv2 
import numpy as np 




img = cv2.imread('../098.picture/ImageCreate.jpg', cv2.IMREAD_UNCHANGED)
 # 設置卷積核 
kernel = np.ones((16, 16), np.uint8) 
erosion = cv2.erode(img,kernel,iterations = 1) 
cv2.imshow('img', img)
cv2.imshow('erosion', erosion)
cv2.imshow('different', img-erosion)

 
cv2.waitKey(0) 
cv2.destroyAllWindows()

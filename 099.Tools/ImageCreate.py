import numpy as np
import cv2

#*****************
high = 256
center =high/2
center_high = 10
#*****************

# 使用Numpy创建一张A4(high*high)纸
img = np.zeros((high,high,1), np.uint8)
# 使用黑色填充图片区域
img.fill(0)
img[int(center)-center_high:int(center)+center_high,int(center)-center_high:int(center)+center_high]=255

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite('ImageCreate.jpg',img)
cv2.destroyAllWindows()
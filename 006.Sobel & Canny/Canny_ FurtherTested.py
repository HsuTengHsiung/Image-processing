import cv2
import numpy as np

img = cv2.imread('../098.picture/People.jpg',0)
'''
由於Canny只能處理灰度圖，所以將讀取的影象轉成灰度圖。
用高斯平滑處理原影象降噪。
呼叫Canny函式，指定最大和最小閾值，其中apertureSize預設為3。
'''
for i in range (3,11,2):
    img_Blur = cv2.GaussianBlur(img, (i, i), 0)  
    canny = cv2.Canny(img_Blur, 50, 150)
    cv2.imwrite('./Canny_FurtherTest/canny_Blur/' + str(i)+ '_img' +'.jpg',img_Blur)
    cv2.imwrite('./Canny_FurtherTest/canny_Blur/' + str(i) +'.jpg',canny)
    cv2.imshow( str(i) +'.jpg', canny)
# =============================================================================
# cv2.imshow("orign", img)
# cv2.imshow('Canny', canny)
# cv2.imwrite('./Canny_FurtherTest/canny_test/' + 'img' +'.jpg',img)
# cv2.imwrite('./Canny_FurtherTest/canny_test/' + 'canny' +'.jpg',canny)
# =============================================================================

cv2.waitKey(0)
cv2.destroyAllWindows()

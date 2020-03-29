import cv2


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.imread('../WhyNot.jpg')
# =============================================================================
# cv2.imshow('org', img)
# =============================================================================
cv2.imwrite('./result/org.jpg',img)

img = cv2.imread('../WhyNot.jpg',0) #直接读为灰度图像
# =============================================================================
# cv2.imshow('gray', img)
# =============================================================================
cv2.imwrite('./result/gray.jpg',img)

ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化
# =============================================================================
# cv2.imshow('threshold', img)
# =============================================================================
cv2.imwrite('./result/threshold.jpg',img)

#total=(i_max+1)*j_max
i_max=24
j_max=4

for i in range(0,i_max):
    for j in range(1,j_max):    
        Closing= cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=i*j_max+j)
    cv2.imwrite('./result/' + str(i)+'.jpg',Closing)
# =============================================================================
#     cv2.imshow('Close' +str(i), Closing_25)
# =============================================================================
    
# =============================================================================
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

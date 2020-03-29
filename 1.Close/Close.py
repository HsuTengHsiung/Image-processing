import cv2


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.imread('../WhyNot.jpg')
img = cv2.imread('../WhyNot.jpg',0) #直接读为灰度图像

cv2.imshow('org', img)
ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化
cv2.imshow('threshold', img)

for i in range(0,3):
    for j in range(1,25):    
        opening_25 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=i*25+j)
    cv2.imshow('open' +str(i), opening_25)


cv2.waitKey(0)
cv2.destroyAllWindows()
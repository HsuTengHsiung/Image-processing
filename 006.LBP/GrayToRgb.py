import cv2
image1 =cv2.imread('../098.picture/Road_2_gray.jpg',2)
cv2.imshow("gray",image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../098.picture/coin.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
cv2.imshow("sure_bg",sure_bg)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv2.imshow("sure_fg",sure_fg)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

cv2.imshow("unknown",unknown)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
print(markers)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
print(markers)
plt.hist(markers.ravel(), 42, [-1, 40])
plt.show()
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
cv2.imshow("marker1",markers)

print(markers.shape)
print(type(markers))
print("***")
print(markers)
print("***")
markers1 = cv2.watershed(img,markers)
print(markers1)
print("***")
print(markers)
plt.hist(markers.ravel(), 42, [-1, 40])
plt.show()

thresh[markers1 == -1] = [125]
img[markers1 == -1] = [0,255,0]
print(thresh.shape)
print(markers.shape)
markers =markers*10
cv2.imwrite("markers.jpg",markers)
cv2.imwrite("markers1.jpg",markers1)
cv2.imshow("thresh",thresh)
cv2.imshow("img",img)
cv2.imwrite('../098.picture/water_img.jpg',img)
# =============================================================================
# Final = cv2.addWeighted(thresh,0.5,img,0.5,0)
# cv2.imshow("Final",Final)
# =============================================================================
cv2.waitKey(0)
cv2.destroyAllWindows()
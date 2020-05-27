import matplotlib.pyplot as plt
import cv2
import numpy as np


raw_image_gray=cv2.imread("../098.picture/BlockTest/Road16.jpg",0)
raw_image=cv2.imread("../098.picture/Road/Road_16.jpg")
raw_image_2 = raw_image.copy()
ret, markers = cv2.connectedComponents(raw_image_gray)
cv2.imwrite('../098.picture/markers_block.jpg',markers*10)

dist_transform = cv2.distanceTransform(markers,cv2.DIST_L2,5)
cv2.imshow("dist_transform",dist_transform)
ret, dist_transform = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv2.imshow("dist_transform_0",dist_transform)


plt.hist(markers.ravel(), 42, [-1, 40])
plt.show()
cv2.imwrite('markers_0.jpg',markers)
print(type(markers))
cv2.imshow("markers",markers )
# =============================================================================
# markers = markers*100 
# ===========================================================================
# =============================================================================
# cv2.imwrite('markers.jpg',markers)
# =============================================================================


markers = cv2.watershed(raw_image,markers)
# =============================================================================
# plt.hist(markers.ravel(), 42, [-1, 40])
# plt.show()
# =============================================================================
print( np.max(markers))
print(len(markers))
raw_image[markers == -1] = [255,255,51]
for i in range(0,np.max(markers)):
    raw_image[markers == i] =np.random.randint(0, 256, size=(1, 3))

raw_image_2 = cv2.addWeighted(raw_image,0.7,raw_image_2,0.3,0)
markers = markers*100 
cv2.imwrite('../098.picture/markers.jpg',markers)
cv2.imwrite('../098.picture/raw_image.jpg',raw_image )
cv2.imwrite('../098.picture/raw_image_2.jpg',raw_image_2 )

# cv2.imwrite('markers.jpg',markers)
cv2.imshow("raw_image",raw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
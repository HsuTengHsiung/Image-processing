from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

raw_image_gray=cv2.imread("../098.picture/BlockTest/LBP_noClose.jpg",0)
raw_image=cv2.imread("../098.picture/Road/Road_5.jpg")

ret, markers = cv2.connectedComponents(raw_image_gray)
cv2.imwrite('markers_0.jpg',markers*10)
print(type(markers))
plt.hist(markers.ravel(), 42, [-1, 40])
plt.show()
cv2.imshow("markers",markers )
# =============================================================================
# markers = markers*100 
# =============================================================================
# =============================================================================
# cv2.imwrite('markers.jpg',markers)
# =============================================================================


markers = cv2.watershed(raw_image,markers)
plt.hist(markers.ravel(), 42, [-1, 40])
plt.show()
raw_image[markers == -1] = [255,255,51]
raw_image[markers == 1] = [255,0,0]
raw_image[markers == 2] = [0,255,0]
raw_image[markers == 3] = [0,0,255]
raw_image[markers == 5] = [255,255,255]

markers = markers*100 
cv2.imwrite('markers.jpg',markers)
cv2.imwrite('raw_image.jpg',raw_image )

# cv2.imwrite('markers.jpg',markers)
cv2.imshow("raw_image",raw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
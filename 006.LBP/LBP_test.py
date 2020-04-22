from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
np.set_printoptions(threshold=np.inf)
# settings for LBP
radius = 5  # LBP算法中范围半径的取值
n_points = radius*radius-1
# =============================================================================
# n_points = 8 * radius # 领域像素点数
# =============================================================================
# 读取图像
image1 =cv2.imread('../098.picture/Road_5.jpg')
cv2.imshow("image1",image1)

plt.hist(image1.ravel(), 255, [0, 256])
plt.show()

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret,gray = cv2.threshold(gray,80,255,cv2.THRESH_BINARY)#二值化
gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow("gray",gray)
# =============================================================================
# cv2.imwrite("../098.picture/Road_2_gray.jpg",)
# =============================================================================

# 畫出直方圖
plt.hist(gray.ravel(), 255, [0, 256])
plt.show()


lbp = local_binary_pattern(image1, n_points, radius)
print(lbp.shape)
# =============================================================================
# img_RGB = cv2.merge((lbp,lbp,))
# cv2.imshow("img_RGB",img_RGB)
# =============================================================================
# =============================================================================
# cv2.imshow("lbp_0",lbp)
# lbp[lbp == 0] = 255
# =============================================================================
cv2.imshow("lbp",lbp)
plt.hist(lbp.ravel(), 255, [0, 256])
plt.show()
# =============================================================================
# print(lbp.ravel())
# =============================================================================

edges = filters.sobel(image1)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

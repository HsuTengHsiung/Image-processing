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
radius = 1  # LBP算法中范围半径的取值
n_points = radius*8
# =============================================================================
# n_points = 8 * radius # 领域像素点数
# =============================================================================
# 读取图像
image1 =cv2.imread('../098.picture/Road_5.jpg')
cv2.imshow("image1",image1)

plt.hist(image1.ravel(), 255, [0, 256])
plt.show()

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

lbp_NOror = local_binary_pattern(image1, n_points, radius,method ='default')
lbp_ror = local_binary_pattern(image1, n_points, radius,method ='ror')

cv2.imshow("lbp_NOror",lbp_NOror)
plt.hist(lbp_NOror.ravel(), 255, [0, 256])
plt.show()

cv2.imshow("lbp_ror",lbp_ror)
plt.hist(lbp_ror.ravel(), 255, [0, 256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data, io,data_dir,filters, feature
from skimage.color import label2rgb
import skimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

radius = 1  # LBP算法中范围半径的取值
n_points = radius*8

img = cv2.imread("../098.picture/Road/Road_10.jpg",0)
img_compire = cv2.imread("../098.picture/Sample/Road_10_justroad.jpg",0)
# 计算图img的直方图


image_lbp = local_binary_pattern(img, n_points, radius,method ='ror')
image_lbp2 = local_binary_pattern(img, n_points, radius,method ='ror')
img_compire_lbp = local_binary_pattern(img_compire, n_points, radius,method ='ror')


H1 = cv2.calcHist([img_compire_lbp.astype('uint8')], [0], None, [512],[0,512])
H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1) # 对图片进行归一化处理
 
# 计算图img2的直方图
Block_high = 10*4
h,w = image_lbp.shape
for i in range (0,int(w/Block_high)):
    for j in range(0,int(h/Block_high)):
        x=i*Block_high
        y=j*Block_high
        H2 = cv2.calcHist([image_lbp[y:y+Block_high,x:x+Block_high].astype('uint8')], [0], None, [512],[0,512])
        H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)
         
        # 利用compareHist（）进行比较相似度
        similarity = cv2.compareHist(H1, H2, cv2.HISTCMP_CORREL)
        print(similarity)
        if (similarity>0.9):
            image_lbp[y:y+Block_high,x:x+Block_high]=255
# =============================================================================
#             print("大")
# =============================================================================
        else:
            image_lbp[y:y+Block_high,x:x+Block_high]=0
# =============================================================================
#             print("小")
# =============================================================================

print(i,j)
cv2.imshow("image_lbp",image_lbp)
cv2.imshow("img_compire_lbp",img_compire_lbp)
Final = cv2.addWeighted(image_lbp,0.5,image_lbp2,0.5,0)
cv2.imshow("Final",Final)


cv2.imwrite('../098.picture/Block_test_forRoad10.jpg',image_lbp)
cv2.imwrite('../098.picture/Block_test_Final_forRoad10.jpg',Final)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img和img1直方图展示
plt.subplot(2, 1,1)
plt.plot(H1)
plt.subplot(2,1,2)
plt.plot(H2)
plt.show()

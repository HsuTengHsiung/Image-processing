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

raw_image=cv2.imread("../098.picture/Road_5.jpg")
img = cv2.cvtColor(raw_image,cv2.COLOR_BGR2GRAY)
img_compire = cv2.imread("../098.picture/Sample/Road_3_justroad.jpg",0)
# 计算图img的直方图

method_lbp='ror'
# =============================================================================
# method_lbp='default'
# =============================================================================

image_lbp = local_binary_pattern(img, n_points, radius,method =method_lbp)
image_lbp2 = local_binary_pattern(img, n_points, radius,method =method_lbp)
img_compire_lbp = local_binary_pattern(img_compire, n_points, radius,method =method_lbp)


H1 = cv2.calcHist([img_compire_lbp.astype('uint8')], [0], None, [256],[0,256])
H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1) # 对图片进行归一化处理
 
# 计算图img2的直方图
Block_high = 10*12
Block_high_2 = 10*3
h,w = img.shape
print(h,w)
once = [[]]
image_lbp_copy = image_lbp.copy()
for i in range (0,int(w/Block_high)):
    for j in range(0,int(h/Block_high)):
        x=i*Block_high
        y=j*Block_high
        H2 = cv2.calcHist([image_lbp[y:y+Block_high,x:x+Block_high].astype('uint8')], [0], None, [256],[0,256])
        H2 = cv2.normalize(H2, H2, 0, 1, cv2.NORM_MINMAX, -1)
        similarity = cv2.compareHist(H1, H2, cv2.HISTCMP_CORREL)
# =============================================================================
#         print(similarity)
# =============================================================================
        if (similarity>0.85):
            image_lbp[y:y+Block_high,x:x+Block_high]=255
            
            for k in range(0,int(Block_high/Block_high_2)):
                for l in range(0,int(Block_high/Block_high_2)):
                    x_2=k*Block_high_2
                    y_2=l*Block_high_2
                    H3 = cv2.calcHist([image_lbp_copy[y+y_2:y+y_2+Block_high_2,x+x_2:x+x_2+Block_high_2].astype('uint8')], [0], None, [256],[0,256])
                    H3 = cv2.normalize(H3, H3, 0, 1, cv2.NORM_MINMAX, -1)
                    similarity = cv2.compareHist(H1, H3, cv2.HISTCMP_CORREL)
# =============================================================================
#                     print(similarity)
# =============================================================================
                    if(similarity>0.95):
                        image_lbp_copy[y+y_2:y+y_2+Block_high_2,x+x_2:x+x_2+Block_high_2]=255
                        raw_image[y+y_2:y+y_2+Block_high_2,x+x_2:x+x_2+Block_high_2]=125
                    else:
                        image_lbp_copy[y+y_2:y+y_2+Block_high_2,x+x_2:x+x_2+Block_high_2]=127
        else:
            image_lbp[y:y+Block_high,x:x+Block_high]=0
            image_lbp_copy[y:y+Block_high,x:x+Block_high]=0
print(i,j)
cv2.imshow("image_lbp",image_lbp)
cv2.imshow("img_compire_lbp",img_compire_lbp)
Final = cv2.addWeighted(image_lbp,0.5,image_lbp2,0.5,0)
Final_2 = cv2.addWeighted(image_lbp_copy,0.5,image_lbp2,0.5,0)
cv2.imshow("Final",Final)


cv2.imwrite('../098.picture/BlockTest/Block_test_forRoad5.jpg',image_lbp)
cv2.imwrite('../098.picture/BlockTest/Block_test_forRoad5_2.jpg',image_lbp_copy)
cv2.imwrite('../098.picture/BlockTest/Block_test_Final_forRoad5.jpg',Final)
cv2.imwrite('../098.picture/BlockTest/Block_test_Final2_forRoad5.jpg',Final_2)
cv2.imwrite('../098.picture/BlockTest/Block_test_Final2_forRoad5_raw_image.jpg',raw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img和img1直方图展示
plt.subplot(2, 1,1)
plt.plot(H1)
plt.subplot(2,1,2)
plt.plot(H2)
plt.show()

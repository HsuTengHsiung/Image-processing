import cv2
import numpy as np
import os

path='../098.picture/'
DIR = path #要統計的資料夾
V_temp = None
W_max = 3 #目前參數若要調整先把下方初始影像註解
flag = True
j = 0 
i = 0
path_file_number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(path_file_number)
#********************************************************
# =============================================================================
# img =['org.jpg','gray.jpg','threshold.jpg']
# temp = cv2.imread(path + 'org.jpg')
# next_image = cv2.imread(path + img[1])
# for i in range(2,len(img)):
#     temp = np.hstack((temp,next_image))
#     next_image = cv2.imread(path + img[i])
#     
# temp = np.hstack((temp,next_image))
# V_temp = temp
# flag = False
# print(V_temp.shape)
# =============================================================================
#********************************************************

temp = cv2.imread(path + '0.jpg')
for i in range(2, path_file_number+1-2):
    next_image = cv2.imread(path + str(i-1) + '.jpg')
    if i-j*W_max > W_max :
        if flag:
            flag = False
            V_temp = temp
        else:
            print(temp.shape)
            print(V_temp.shape)
            cv2.imshow('temp',temp)
            cv2.imshow('V_temp',V_temp)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            V_temp = np.vstack((V_temp,temp))
        temp = next_image
        i = i+1
        j = j+1
    else:
        temp = np.hstack((temp,next_image))
        
if i-j*W_max == W_max and not flag:
    V_temp = np.vstack((V_temp,temp))
    
if flag :
    V_temp = temp

cv2.imwrite(path +'merge.jpg', V_temp)
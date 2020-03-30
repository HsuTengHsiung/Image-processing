import cv2
import numpy as np
import os

path='./result/'
W_max = 2 
flag = True
j= 0
# =============================================================================
# img1 = cv2.imread('../WhyNot.jpg')
# img2 = cv2.imread('../WhyNot.jpg')
# temp = np.hstack((img1,img2))
# cv2.imwrite('merge.jpg',temp)
# =============================================================================
img =['org.jpg','gray.jpg','threshold.jpg']
DIR = path #要統計的資料夾
path_file_number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
print(path_file_number)
temp = cv2.imread(path + 'org.jpg')
next_image = cv2.imread(path + img[1])

print(len(img))
for i in range(0,len(img)):
    temp = np.hstack((temp,next_image))
    next_image = cv2.imread(path + img[i])
    

for i in range(0, path_file_number-len(img)):
    if i+len(img)-(j*W_max) >= W_max :
        if flag:
            V_temp = temp
        else:
            print(temp.shape)
            print(V_temp.shape)
            cv2.imshow('temp',temp)
            cv2.imshow('V_temp',V_temp)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            V_temp = np.vstack((V_temp,temp))
        flag = False
        temp = next_image
        i = i+1
        j=j+1
        next_image = cv2.imread(path + str(i) +'.jpg' )
    print(i)
    temp = np.hstack((temp,next_image))
    next_image = cv2.imread(path + str(i) +'.jpg' )

temp = np.hstack((temp,next_image))
temp = np.hstack((temp,next_image))

V_temp = np.vstack((V_temp,temp))

cv2.imwrite('merge.jpg',V_temp)

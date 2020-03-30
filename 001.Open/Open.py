import cv2
import time
import warnings
import os
warnings.filterwarnings('ignore')

for k in range(3,10):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k,k))
    img = cv2.imread('../WhyNot.jpg')
    # =============================================================================
    # cv2.imshow('org', img)
    # =============================================================================
    cv2.imwrite('./result/org.jpg',img)
    
    img = cv2.imread('../WhyNot.jpg',0) #直接读为灰度图像
    # =============================================================================
    # cv2.imshow('gray', img)
    # =============================================================================
    cv2.imwrite('./result/gray.jpg',img)
    
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#二值化
    # =============================================================================
    # cv2.imshow('threshold', img)
    # =============================================================================
    cv2.imwrite('./result/threshold.jpg',img)
    
    i_max=24
    j_max=4
    
    
    org = (40, 80)
    fontFace = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 3
    # =============================================================================
    # fontcolor = (0, 255, 0) # BGR
    # =============================================================================
    fontcolor = 255 # BGR
    thickness = 1 
    lineType = 4
    bottomLeftOrigin = 1
    
    #total=(i_max+1)*j_max
# =============================================================================
#     print(kernel)
# =============================================================================
    print('\r\n\r\n','kernel=' ,k,'x',k )
    for i in range(0,i_max+1):
        for j in range(1,j_max):
            start = time.clock()
            for z in range(0,i*j_max+j):
                img= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
            end = time.clock()
        text = 'Number:' + str( (i+1)*j_max ) + ' ' + str(end-start)
        print(text)
        cv2.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
        save_path = './result/' + str(k) + '/'
        if not os.path.isdir(save_path):
            os.mkdir(save_path)
        cv2.imwrite('./result/' + str(k) + '/' +  str(i)+'.jpg',img)
    # =============================================================================
    #     cv2.imshow('Open' +str(i), Closing_25)
    # =============================================================================
        
    # =============================================================================
    # 
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # =============================================================================

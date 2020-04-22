import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

image =cv2.imread('../098.picture/Road_2.jpg')
# =============================================================================
# cv2.imshow("gray",image)
# 
# =============================================================================

image_slic = seg.slic(image,n_segments = 200)
# =============================================================================
# image_show(color.label2rgb(image,image,kind ='avg'))
# =============================================================================
image_show(color.label2rgb(image_slic,image,kind ='avg'))
cv2.imwrite("../098.picture/Road_2_image_slic.jpg",color.label2rgb(image_slic,image,kind ='avg'))

# =============================================================================
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================
image_felzenszwalb = seg.felzenszwalb(image)
image_show(image_felzenszwalb)
np.unique(image_felzenszwalb).size

image_felzenszwalb_colored = color.label2rgb(image_felzenszwalb, image, kind='avg')
image_show(image_felzenszwalb_colored)
cv2.imwrite("../098.picture/Road_2_image_felzenszwalb.jpg",image_felzenszwalb)
cv2.imwrite("../098.picture/Road_2_image_felzenszwalb_colored.jpg",image_felzenszwalb_colored)

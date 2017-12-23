import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('path/name_img',0)
#cv2.startWindowThread()
cv2.namedWindow("preview",cv2.WINDOW_NORMAL)
cv2.imshow("preview", img) 
k=cv2.waitKey()
if k==27:
    x=1
elif k==ord('s'):
    cv2.imwrite('path/name_img',img)
    cv2.destroyAllWindows()

'''
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()'''

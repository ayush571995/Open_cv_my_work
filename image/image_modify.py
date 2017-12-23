import cv2
import numpy as np
img=cv2.imread('/home/ayush/Desktop/faltu/IMG_20160106_172031.jpg')
from matplotlib import pyplot as plt
BLUE=[0,0,255]
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
cv2.imshow('image',img)
k=cv2.waitKey(0) & 0xFF
if k==ord('q'):
    cv2.destroyAllWindows()

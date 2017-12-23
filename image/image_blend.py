import cv2
img1=cv2.imread('path/name_img_1')
img2=cv2.imread('path/name_img_2.jpg')
dst=cv2.addWeighted(img1,0.9,img2,0.9,3)
cv2.namedWindow('final',cv2.WINDOW_NORMAL)
cv2.imshow('final',dst)
k=cv2.waitKey(0) & 0xFF
if k==ord('q'):
    cv2.destroyAllWindows()

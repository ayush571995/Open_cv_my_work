import os
import cv2,time
absolute_path_list=[]
for root,dirs,files in os.walk("path",topdown=False):
    for names in files:
        if '.JPG' in names:
            absolute_path_list.append(os.path.join(root,names))
for index in range(len(absolute_path_list)-1):
    img1=cv2.imread(absolute_path_list[index])
    img2=cv2.imread(absolute_path_list[index+1])
    cv2.namedWindow('slideshow',cv2.WINDOW_NORMAL)
    alpha=1.0
    beta=0.0
    while beta<=1.0:
        dst=cv2.addWeighted(img1,alpha,img2,beta,0)
        alpha-=0.2
        beta+=0.2
        cv2.imshow('slideshow',dst)
        k=cv2.waitKey(1) & 0xFF
        if k==ord('q'):
            cv2.destroyAllWindows()
            exit(0)
    time.sleep(1)
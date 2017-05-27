import numpy as np
import cv2
def line(img,x1,y1,x2,y2):
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
def rectangle(img,x1,y1,x2,y2):
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
def circle(img,x1,y1,r):
    cv2.circle(img,(x1,y1),r,(0,255,0),3)
def ellipse(img,x1,y1,m1,m2,aa1,aa2,ca1,ca2):
    cv2.ellipse(img,(x1,y1),(m1,m2),aa1,aa2,ca1,ca2,3)
img=img=np.zeros((512,512,3),np.uint8)
print('Enter shape of canvas ')
ch=input('1. Line\n2.Rectangle\n3.Circle\n4.Ellipse')
if ch.lower()=='1':
    print('input coordinates seperated by spaces')
    x1,y1,x2,y2=input().split(' ')
    line(img,int(x1),int(y1),int(x2),int(y2))
    cv2.imshow('image',img)
    cv2.waitKey(0)&0xFF
elif ch.lower()=='2':
    print('input coordinates seperated by spaces')
    x1,y1,x2,y2=input().split(' ')
    rectangle(img,int(x1),int(y1),int(x2),int(y2))
    cv2.imshow('image',img)
    cv2.waitKey(0)&0xFF
elif ch.lower()=='3':
    print('input centre cordinates and radius seperated by spaces')
    x1,y1,r=input().split(' ')
    circle(img,int(x1),int(y1),int(r))
    cv2.imshow('image',img)
    cv2.waitKey(0)&0xFF
elif ch.lower()=='4':
    print('input centre cordinates len of major and minor axis 4 angles ')
    x1,y1,m1,m2,aa1,aa2,ca1,ca2=input().split(' ')
    ellipse(img,int(x1),int(y1),int(m1),int(m2),int(aa1),int(aa2),int(ca1),int(ca2))
    cv2.imshow('image',img)
    cv2.waitKey(0)&0xFF
    

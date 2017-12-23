import cv2

def sketch(img):

    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray,(7,7),0)
    canny_edges = cv2.Canny(img_gray_blur,10,70)
    ret,mask = cv2.threshold(canny_edges,120,255,cv2.THRESH_BINARY_INV)
    return mask

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = sketch(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
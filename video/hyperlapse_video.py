import cv2
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
dim=(int(cap.get(3)),int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
l=[]
speed=30
cv2.namedWindow('frame')
cv2.createTrackbar('speed','frame',0,2,nothing)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        l.append(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            slider_pos=cv2.getTrackbarPos('speed', 'frame')
            break
    else:
        break
if slider_pos==1:
    speed=60.0
elif slider_pos==2:
    speed=120.0
out = cv2.VideoWriter('output.avi', fourcc, speed, dim)
# Release everything if job is finished
for i in l:
    out.write(i)
cap.release()
out.release()
cv2.destroyAllWindows()


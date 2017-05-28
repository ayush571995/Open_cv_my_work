import os,cv2,time
class Slideshow:


    def __init__(self,path,time=3):
        self.absolute_path_list=[]
        self.time=time
        for root,dirs,files in os.walk(path,topdown=False):
            for names in files:
                if '.jpg' in names or '.JPG' in names or '.png' in names or '.PNG' in names :
                    self.absolute_path_list.append(os.path.join(root,names))
        self.length_list=len(self.absolute_path_list)

    def start_slideshow(self):
        for index in range(self.length_list):
            img1=cv2.imread(self.absolute_path_list[index])
            cv2.namedWindow('slideshow',cv2.WINDOW_NORMAL)
            cv2.imshow('slideshow', img1)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('q') or k==27:
                cv2.destroyAllWindows()
                exit(0)
            time.sleep(self.time)


ob=Slideshow('/home/ayush/Desktop/',3)
ob.start_slideshow()
import cv2
import os
path="PRO-C105-Student-Boilerplate-main/Images"
allimages=os.listdir(path)
images=[]
for i in allimages: 
    anewpath=path+"/"+i
    images.append(anewpath)
frame=cv2.imread(images[0])
height, width,channels=frame.shape
size=(width,height)
newvideo=cv2.VideoWriter("sunrise.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in reversed(images):
    frame=cv2.imread(i)
    newvideo.write(frame)
newvideo.release()
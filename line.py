import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=cv2.line(frame,(0,0),(width,height),(250,0,0),10)
    img=cv2.line(img,(0,height),(width,0),(0,200,0),10)
    img=cv2.rectangle(img,(100,100),(200,200),(128,128,27),5)
    img=cv2.circle(img,(200,200),(60),(0,0,250),10)
    font=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(img,'Pooja is Great!',(10,height-10),font,1,(40,100,0),2,cv2.LINE_AA)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release
cv2.destroyAllWindows()


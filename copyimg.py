import cv2
 
img=cv2.imread('asserts\pic3.jpg',-1)
img=cv2.resize(img,(400,400))

tag=img[200:300,150:250]
img[200:300,300:400]=tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



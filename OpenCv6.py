import cv2
import numpy as np

img = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\opencv-python-filtering-example.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

dus_kir = np.array([30,150,50])
yuk_kir= np.array([255,255,255])

mask = cv2.inRange(hsv,dus_kir,yuk_kir)
res = cv2.bitwise_and(img,img,mask=mask)
  
kernal = np.ones((15,15),np.float32)/255
smoothed =cv2.filter2D(res,-1,kernal)
median = cv2.medianBlur(res,15)
    

cv2.imshow("img",img)
cv2.imshow("mask",mask)
cv2.imshow("res",res)
cv2.imshow("smoothed",smoothed)
cv2.imshow("median",median)

cv2.waitKey(0)
cv2.destroyAllWindows()
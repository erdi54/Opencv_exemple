import cv2
import numpy as np


img1 = cv2.imread(r"C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\opencv-corner-detection-sample.jpg")
gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)
print(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img1,(x,y),3,255,-1)


cv2.imshow('kose', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

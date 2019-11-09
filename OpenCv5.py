import cv2
import numpy as np

# Load two images
img = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\bookpage.jpg')
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,thrashold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
th =cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
cv2.imshow('res',img)
cv2.imshow('eşikleme',th)
cv2.imshow("gri",gri)
ret2,th2 = cv2.threshold(gri,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("es2",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
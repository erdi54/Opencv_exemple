import cv2
import numpy as np

# 500 x 250
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\3D-Matplotlib.png')
img2 = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\mainsvmimage.png')

add = img1+img2

cv2.imshow('add',add)
 
add2 = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('add2',add2)

cv2.waitKey(0)
cv2.destroyAllWindows()
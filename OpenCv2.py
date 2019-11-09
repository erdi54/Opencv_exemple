import cv2

img = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\res1.jpg', cv2.IMREAD_COLOR)
scale_percent = 160 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
px =img[10:60,10:80]
img[10:60,10:80]=[255,255,255]
img[60:110,90:160]= px
cv2.imshow('deneme',resized)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
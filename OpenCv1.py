import cv2

img = cv2.imread(r'C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\res1.jpg', cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
font = cv2.FONT_HERSHEY_SIMPLEX
context = input("Message")
cv2.putText(img,context,(10,50),font,1,(0,200,250),2,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

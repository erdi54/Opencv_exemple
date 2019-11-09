import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(r"C:\Users\erdiozcan.Erdi\Desktop\OpenCv_Ex\people-walking.mp4")
fgbr = cv2.createBackgroundSubtractorMOG2()
while (1):
    ret,frame = cap.read()
    fgmask = fgbr.apply(frame)

    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() 
cv2.destroyAllWindows()

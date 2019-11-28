# this is a demo for opencv
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Can not open camera!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame ...")
        break

   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    #cv2.imshow('gray video', gray)
    cv2.imshow('gray video', frame)
    key = cv2.waitKey(24)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


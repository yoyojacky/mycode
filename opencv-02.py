#save video
# 
import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (800, 480), True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can not receive frame...")
        break 
    for i in range(18):
        print(i, ":", cap.get(i))
    frame = cv2.flip(frame, 0)
    out.write(frame)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# release all
cap.release()
out.release()
cv2.destroyAllWindows()

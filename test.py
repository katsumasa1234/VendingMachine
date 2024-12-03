import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("Y", "U", "Y", "V"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
while(True):
    ret, img = cap.read()
    if not ret:
        continue
    print(img)
    cv2.imshow("capture", img)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
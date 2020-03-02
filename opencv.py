import cv2,time
import matplotlib as plt
import numpy as np

#capture a single photo
video = cv2.VideoCapture(0)
check,frame = video.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow("capturing",frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows

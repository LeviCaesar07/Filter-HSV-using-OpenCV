import cv2
import numpy as np

max_value=255
max_value_H=360//2
low_H=0
low_S=0
low_V=0
high_H=max_value_H
high_S=max_value
high_V=max_value
window_detection_name='Result'
low_H_name='Low H'
low_S_name='Low S'
low_V_name='Low V'
high_H_name='High H'
high_S_name='High S'
high_V_name='High V'

def on_low_H_thresh_trackbar(val):
	global low_H
	global high_H
	low_H=val
	low_H=min(high_H-1,low_H)
	cv2.setTrackbarPos(low_H_name, window_detection_name,low_H)

def on_High_H_thresh_trackbar(val):
	global low_H
	global high_H
	high_H=val
	high_H=max(high_H,low_H+1)
	cv2.setTrackbarPos(high_H_name, window_detection_name,high_H)

def on_low_S_thresh_trackbar(val):
	global low_S
	global high_S
	low_S=val
	low_S=min(high_S-1,low_S)
	cv2.setTrackbarPos(low_S_name, window_detection_name,low_S)

def on_High_S_thresh_trackbar(val):
	global low_S
	global high_S
	high_S=val
	high_S=max(high_S,low_S+1)
	cv2.setTrackbarPos(high_H_name, window_detection_name,high_S)

def on_low_V_thresh_trackbar(val):
	global low_V
	global high_V
	low_V=val
	low_V=min(high_V-1,low_V)
	cv2.setTrackbarPos(low_V_name, window_detection_name,low_V)

def on_High_V_thresh_trackbar(val):
	global low_V
	global high_V
	high_V=val
	high_V=max(high_V,low_V+1)
	cv2.setTrackbarPos(high_V_name, window_detection_name,high_V)

img=cv2.VideoCapture(0)

cv2.namedWindow(window_capture_name)
cv2.namedWindow(window_detection_name)

cv2.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_High_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, window_detection_name, high_H, max_value, on_High_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_High_V_thresh_trackbar)


while True:
	ret,frame=img.read()
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv, (low_H,low_S,low_V), (high_H,high_S,high_V))
	ret=cv2.bitwise_and(frame,frame, mask=mask)

	data=np.hstack((frame, hsv))
	cv2.imshow('Stack', data)
	cv2.imshow(window_detection_name,mask)
	if cv2.waitKey(1)&0XFF==ord('q'):
		break

img.release()
cv2.destroyAllWindows()
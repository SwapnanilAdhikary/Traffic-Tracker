from ultralytics import YOLO
import cv2
model = YOLO("traffic.pt")
result = model('4K Road traffic video for object detection and tracking - free download now!.mp4',show=True)
cv2.waitKey()
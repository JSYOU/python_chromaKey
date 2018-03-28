import cv2
import numpy as np

lower_color = np.array([40,90,90])
upper_color = np.array([120,250,250])

def chromaKey(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    inv_mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(image,image,mask= inv_mask)
    return res
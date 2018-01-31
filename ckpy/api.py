import cv2
import numpy as np


lower_color = np.array([40,90,90])
upper_color = np.array([120,200,200])

def chromaKey(image):

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)
    inv_mask = cv2.bitwise_not(mask)

    # Bitwise-AND mask,inv_mask and original image
    res = cv2.bitwise_and(image,image,mask= inv_mask)
    return res
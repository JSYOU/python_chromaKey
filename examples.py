import ckpy
import cv2

image = cv2.imread("./test.jpg")

res = ckpy.chromaKey(image)

while(1):
    cv2.imshow('res',res)
    k = cv2.waitKey(60) 
    if k == 27:
        break
# python_chromaKey
### dependencies
`Python version` - 2.7 or 3
`openCV version` - 2.4 or 3.3
### How to use
#### Use image file
```python
import ckpy
##You can use cv2.imread("image") or io.imread("image") load image
img = cv2.imread("./image_file")
res = ckpy.chromaKey(img)
cv2.imshow('res',res)
```
#### Use webcam
```python
import ckpy
cap = cv2.VideoCapture(0)
while (1):
    ret, frame = cap.read()
    res = ckpy.chromaKey(frame)
    cv2.imshow('frame',frame)
```

#### Res will show a photo or video from the subject of remove a background 

#### You can mix anything you want in the image

![](https://raw.githubusercontent.com/JSYOU/python_chromaKey/master/test.jpg)
![](https://raw.githubusercontent.com/JSYOU/python_chromaKey/master/res.png)

import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('photos/boston.jpg')
cv.imshow('Boston',img)

#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV(hue saturation value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to LAB
Lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',Lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#hsv t0 bgr
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv_bgr)

plt.imshow(rgb)
plt.show()




cv.waitKey(0)
import cv2 as cv
import numpy as np


img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian
lap=cv.Laplacian(gray,cv.CV_64F)#handle negative values
lap=np.uint8(np.absolute(lap))#convert to 8 bit image
cv.imshow('Laplacian',lap)


#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)




cv.waitKey(0)

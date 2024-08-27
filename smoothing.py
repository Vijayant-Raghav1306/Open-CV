import cv2 as cv
import numpy as np

img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

#Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)
#Gaussian Blur-less blur than average since weight value is added
gauss=cv.GaussianBlur(img,(9,9),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
median=cv.medianBlur(img,8)
cv.imshow('Median Blur',median)

#Bilateral-retains edges used mosytly for ADVANCED CV
bilaretal=cv.bilateralFilter(img,10,35,35)
cv.imshow('Bilateral',bilaretal)

cv.waitKey(0)

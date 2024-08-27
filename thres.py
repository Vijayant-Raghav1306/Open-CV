import cv2 as cv


img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Simple thresholding-used to segment an image by setting pixel values to a specific range. It's commonly used in image processing to create binary images from grayscale images.
threshold,thresh=cv.threshold(gray,225,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)
#to inverse just add THRESH_BINARY_INV

#Adaptive Thresholding-threshold value is calculated on its own,useful when image has varying lighting conditions.has 2 params-1)block size-to find kernel size to compute mean to find the optimal threshold value;2)C-integer sub from mean to fine tune our threshold
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)
import cv2 as cv
import numpy as np
#for creating a blank image
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('BLank',blank)

#Paint the image a certain color
blank[:]=0,255,0
cv.imshow('Green',blank)

#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('Rectangle',blank)

#draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)

#draw a line
cv.line(blank,(100,250),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line',blank)

#write text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)


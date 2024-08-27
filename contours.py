import cv2 as cv

img=cv.imread('photos/cat.jpg')


cv.imshow('Cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#canny=cv.Canny(img,125,175)
#cv.imshow('Canny Edges',canny) first method to find contours by bluring the image and using canny edges

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)#second method is threshold


contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

cv.waitKey(0)

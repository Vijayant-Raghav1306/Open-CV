import cv2 as cv
'''reading images
img= cv.imread('Photos/cat image.jpg')

cv.imshow('Cat',img)
cv.waitKey(0)'''
#reading videos

capture=cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
    



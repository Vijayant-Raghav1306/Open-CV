import cv2 as cv

'''img=cv.imread('Photos/cat image.jpg')
cv.imshow('Cat',img)'''

def rescaleFrame(frame,scale=0.2):
    #for videos,images,live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[1]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
    

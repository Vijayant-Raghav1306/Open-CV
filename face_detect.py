import cv2 as cv

img=cv.imread('photos/lady.jpg')
cv.imshow('Person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade=cv.CascadeClassifier('haar_face_xml')#not the most optimal for adavanced cv projects

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

print(f'Number of faces found={len(faces_rect)}')

for(x,y,w,h)in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow('Detected Faces',img)#sometimes detects other things as faces as it is sensitive to noise in an image.one way to reduce it is to change the minneighbours parameter






cv.waitKey(0)
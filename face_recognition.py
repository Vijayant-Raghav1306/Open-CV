
import cv2 as cv
 
haar_cascade=cv.CascadeClassifier('haar_face_xml')

people=['Ben Affleck','Chris Evans','Shahrukh Khan']
#features=np.load('features.npy')
#labels=np.load('labels.py')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'C:\Users\DELL\Downloads\celeb photos\ben affleck\wp1898873-ben-affleck-wallpapers_11zon.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#Detect the face in the image
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]
    
    label,confidence=face_recognizer.predict(faces_roi)
    print(f'Label={people[label]} with a confidence of {confidence}')
    
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
cv.imshow('Detected Face',img)
cv.waitKey(0)
#I dont have any training dataset we will first have to gather some images and train them in the faces_train.py file then which our code will work perfectly and detect images like of ben affleck with a confidence.

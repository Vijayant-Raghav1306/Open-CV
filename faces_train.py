import os
import cv2 as cv
import numpy as np

people=['Ben Affleck','Chris Evans','Shahrukh Khan']
DIR=r'C:\Users\DELL\Downloads\celeb photos'

features=[]
labels=[]

haar_cascade=cv.CascadeClassifier('haar_face_xml')

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            
            for(x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()
print('Training Done')



print(f'Length of features={len(features)}')
print(f'Length of labels={len(labels)}')

features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and labels list

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)

    
    
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')#pixel intensities-for eg if the peak is from 40 to 70 at around 35000 pixels that means in the regiom from 40 to 70 most of the pixels lie in the range from 35000..
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



#colour histogram
plt.figure()
plt.title()
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
plt.show() 
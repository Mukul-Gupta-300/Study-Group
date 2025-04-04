import cv2 as cv
import numpy as np

img = cv.imread(r"C:\games\coding\coding\Python\images\noise.jpg")
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel=np.ones((6,6),np.float32)/36

dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))
gblur=cv.GaussianBlur(img,(5,5),0)
median=cv.medianBlur(img,5)
bilateralFilter=cv.bilateralFilter(img,9,75,75)



cv.imshow('image', img)
cv.imshow('dst', dst)
cv.imshow('blur', blur)
cv.imshow('gblur', gblur)
cv.imshow('median', median)
cv.imshow('bilateralFilter', bilateralFilter)

cv.waitKey(0)
cv.destroyAllWindows()




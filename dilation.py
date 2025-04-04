import cv2 as cv
import numpy as np

img = cv.imread(r"C:\games\coding\coding\Python\images\smarties.png",0)
_, mask= cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)

dilation=cv.dilate(mask,kernel,iterations=1)
erosion=cv.erode(mask,kernel,iterations=1)
opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
closing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
mg=cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel)
th=cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel)












cv.imshow('image', img)
cv.imshow('mask', mask)
cv.imshow('dilation', dilation)
cv.imshow('erosion', erosion)
cv.imshow('opening', opening)
cv.imshow('closing', closing)
cv.imshow('mg', mg)
cv.imshow('th', th)

cv.waitKey(0)
cv.destroyAllWindows()





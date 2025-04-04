import cv2 as cv
import numpy as np

img = cv.imread(r"C:\games\coding\coding\Python\images\FindingContours.png")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgGray,127,255,0)
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(img,contours,-1,(0,255,255),10)
cv.drawContours(imgGray,contours,0,(0,0,255),10)

cv.imshow('image', img)
cv.imshow('thresh', thresh)
cv.imshow('imageGray', imgGray)

cv.waitKey(0)
cv.destroyAllWindows()









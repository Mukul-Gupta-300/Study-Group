import cv2 as cv
import numpy as np

img = cv.imread(r"C:\games\coding\coding\Python\images\face.webp",0)
lap=cv.Laplacian(img,cv.CV_64F, ksize=3)
lap=np.uint8(np.absolute(lap))
sobleX=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobleY=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)


# sobleX=np.uint8(np.absolute(sobleX))
# sobleY=np.uint8(np.absolute(sobleY))
sobleCombined=cv.bitwise_or(sobleX,sobleY)
edges=cv.Canny(img,100,200)




cv.imshow('image', img)
# cv.imshow('lap', lap)
cv.imshow('sobleX', sobleX)
cv.imshow('sobleY', sobleY)
cv.imshow('sobleCombined', sobleCombined)
cv.imshow('edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()


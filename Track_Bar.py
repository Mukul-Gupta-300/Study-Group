import cv2
import numpy as np

img = np.zeros((300,512,3), np.uint8)

# frame=cv2.imread(r"C:\games\coding\coding\Python\images\face.webp",-1)

def nothing(x):
    return 

cv2.namedWindow("Image")
cv2.createTrackbar("R", "Image", 0,255, nothing)
cv2.createTrackbar("G", "Image", 0,255, nothing)
cv2.createTrackbar("B", "Image", 0,255, nothing)

while(True):
    cv2.imshow("Image", img)
    

    r= cv2.getTrackbarPos("R", "Image")
    g= cv2.getTrackbarPos("G", "Image")
    b= cv2.getTrackbarPos("B", "Image")

    img[:]=[b,g,r]

    cv2.waitKey(1)

    
cv2.destroyAllWindows()
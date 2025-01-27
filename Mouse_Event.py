import cv2

def click_events(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONUP:
        strXY=str(x)+ ' , '+ str(y)



        cv2.putText(frame, strXY, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow('Image', frame)

    if event==cv2.EVENT_RBUTTONUP:
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]

        strRGB=str(blue)+ ' , '+ str(green)+ "  , " + str(red)

        cv2.putText(frame, strRGB, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

        cv2.imshow('Image', frame)




frame=cv2.imread(r"C:\games\coding\coding\Python\images\face.webp",-1)

cv2.imshow("Image", frame)

cv2.setMouseCallback('Image', click_events)


cv2.waitKey(0)

cv2.destroyAllWindows()
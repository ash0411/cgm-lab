import cv2
import numpy as np
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),color,-1)
                print(color)
            else:
                cv2.circle(img,(x,y),5,color,-1)
                print(color)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),color,-1)
            print(color)
        else:
            cv2.circle(img,(x,y),10,color,-1)
            print(color)
            
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    color = (0,255,0)
    key = cv2.waitKey(1) 
    if key == ord('c'):
        mode = False
    elif key == ord('r'):
        mode = True
    elif key == ord('R'):
        color = (255,0,0)
    elif key == ord('b'):
        color = (0,0,255)
    elif key == ord('G'):
        color = (0,255,0)
    elif key == ord('W'):
        color = (255,255,255)
    
    cv2.imshow('image',img)
    
    
    if key & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
# dda
from graphics import *
from math import *
import time
# this is a program to make a line through the dda line making algorithm
def DDA(X0,Y0,X1,Y1):
    win = GraphWin("DDA", 300, 300)
    # calculating delta x and delta y
    dx = X1 - X0 
    dy = Y1 - Y0
    #finding delta with maximum magnitude to make number of steps
    if abs(dx) > abs(dy): 
        steps = abs(dx) 
    else:
        steps = abs(dy)
    # defining increment steps
    Xinc = dx*1.0/steps
    Yinc = dy*1.0/steps
    # initializing initial points
    X = X0
    Y = Y0
    # loop for plotting the circle
    for i in range(0,steps+1):
        c = Point(X,Y)
        c.draw(win)
        X+=Xinc
        Y+=Yinc
        time.sleep(0.01)
    win.getMouse()
# calling function
DDA(2, 2, 150, 220) 
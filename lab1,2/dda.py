# dda
from graphics import *
from math import *
import time

def DDA(X0,Y0,X1,Y1):
    win = GraphWin("DDA", 300, 300)
    dx = X1 - X0
    dy = Y1 - Y0

    if abs(dx) > abs(dy): 
        steps = abs(dx) 
    else:
        steps = abs(dy)

    Xinc = dx*1.0/steps
    Yinc = dy*1.0/steps

    X = X0
    Y = Y0
    for i in range(0,steps+1):
        c = Point(X,Y)
        c.draw(win)
        X+=Xinc
        Y+=Yinc
        time.sleep(0.01)
    win.getMouse()
DDA(2, 2, 200, 200); 
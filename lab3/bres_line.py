from graphics import *
import time
def bres_line(x1,y1,x2,y2):
    win = GraphWin("bres_algo")
    d_x = x2-x1
    d_y = y2-y1
    x = x1
    y = y1
    Point(x1,y1).draw(win)
    p = 2*d_y - d_x
    for i in range(d_x):
        if p<0:
            p = p +2*d_y
            x = x+1
        else:
            p += p + 2*d_y - 2*d_x
            x+=1
            y+=1
        time.sleep(0.5)
        Point(x,y).draw(win)
    win.getKey()
def bres_line1(x1,y1,x2,y2):
    win = GraphWin("bres_algo1")
    d_x = x2-x1
    d_y = y2-y1
    x = x1
    y = y1
    Point(x1,y1).draw(win)
    p = 2*d_y - d_x
    for i in range(d_x):
        if p<0:
            p = p +2*d_x
            y = y+1
        else:
            p += p + 2*d_x - 2*d_y
            x+=1
            y+=1
        time.sleep(0.5)
        Point(x,y).draw(win)
    win.getKey()
bres_line(5,10,50,20)
bres_line1(5,10,50,20)


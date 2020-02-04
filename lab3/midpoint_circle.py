from graphics import *
import time
# a function to plot all the 7 pixels found in symmetric locations
def drawCircle(win,xc,yc,x,y):
    pt1=Point(xc+x, yc+y) 
    pt2=Point(xc-x, yc+y) 
    pt3=Point(xc+x, yc-y) 
    pt4=Point(xc-x, yc-y) 
    pt5=Point(xc+y, yc+x) 
    pt6=Point(xc-y, yc+x) 
    pt7=Point(xc+y, yc-x) 
    pt8=Point(xc-y, yc-x) 
    pt1.draw(win)
    pt2.draw(win)
    pt3.draw(win)
    pt4.draw(win)
    pt5.draw(win)
    pt6.draw(win)
    pt7.draw(win)    
    pt8.draw(win)
# function to implement midpoint algo
def midpoint_circle(x_center,y_center,radius):
    win = GraphWin('m_circle')
    p = 1-radius
    x = 0
    y = radius
    drawCircle(win,x_center,y_center,x,y)
    while y>=x:
        if p<0:
            p = p + 2*x +3
            x += 1
            drawCircle(win,x_center,y_center,x,y)
        else:
            p = p + 2*(x-y) +5
            x +=1
            y = y-1
            drawCircle(win,x_center,y_center,x,y)
        time.sleep(0.5)
    win.getMouse()
x,y,r = input("Enter the coordinates of center of circle as well as radius").split()
midpoint_circle(int(x),int(y),int(r))
        
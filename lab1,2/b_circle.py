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
# function to plot the bresenham's circle
def b_circle(xc,yc,r):
    # initializing initial value of x,y
    x =0
    y = r
    decision_parameter = 3 -(2*r)
    win = GraphWin('b_circle')
    drawCircle(win,xc,yc,x,y)
    while y>x :
        x +=1 # it is incremented in both the cases
        # check for decision parameter to update d,y
        if decision_parameter>0:
            y = y-1
            decision_parameter = decision_parameter + 4*(x-y) +10
        else:
            decision_parameter = decision_parameter +4*x+6
        drawCircle(win,xc,yc,x,y)# for each pixel drawing all 8 pixel
        time.sleep(2) 
    win.getMouse()
help(Point)
b_circle(35,50,30)


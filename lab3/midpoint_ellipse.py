from graphics import *
import time
# to draw symetrical points
def draw_ellipse(win,x_c,y_c,x,y):
    pt1 = Point(x+x_c,y+y_c)
    pt2 = Point(-x+x_c,y+y_c)
    pt3 = Point(-x +x_c,-y+y_c)
    pt4 = Point(x+x_c,-y+y_c)
    pt1.draw(win)
    pt2.draw(win)
    pt3.draw(win)
    pt4.draw(win)
# function to implement midpoint algo 
def midpoint_ellipse(x_c,y_c,a,b):
    win = GraphWin("ellipse")
    x = 0
    y = b
    p = b*b - a*a*b + (a*a)/4
    draw_ellipse(win,x_c,y_c,x,y)
    # for region 1 
    while b*b*x < a*a*y:
        if p <0:
            p = p+2*b*b*x + b*b
            x +=1
        else:
            p = p +2*b*b*x - 2*a*a*y + b*b
            x+=1
            y-=1
        time.sleep(0.5)
        draw_ellipse(win,x_c,y_c,x,y)
    # going to region 2
    p = b*b*(x + 0.5)*(x+0.5)+ a*a*(y-1)*(y-1)-a*a*b*b
    while y != 0:
        if p>0:
            p += -2*a*a*y + a*a
            y-=1
        else:
            p += 2*b*b*x - 2*a*a*y + a*a
        time.sleep(0.5)
        draw_ellipse(win,x_c,y_c,x,y)    
    win.getMouse()
x_c,y_c,a,b = input("enter the coordinates of center as well as the major and minor axis").split()
midpoint_ellipse(int(x_c),int(y_c),int(a),int(b))#calling function
from graphics import *
win = GraphWin("Liang Barsky Line Clipping Algorithm",1000, 1000)
xmin=200
ymin=200
xmax=450
ymax=450
rect = Rectangle(Point(xmin, ymin), Point(xmax, ymax))
rect.draw(win)

x1=int(input("enter x1 "))
y1=int(input("enter y1 "))
x2=int(input("enter x2 "))
y2=int(input("enter y2"))

line = Line(Point(x1,y1),Point(x2,y2))
line.setFill("green")
line.draw(win)

dx=x2-x1
dy=y2-y1


p=[-dx,dx,-dy,dy]
q=[x1-xmin , xmax-x1,y1-ymin , ymax-y1]
t = [None] * len(p)

for i in range(len(p)):
    
    if (p[i]!=0):
        t[i]=float(q[i]/p[i])
        
    else:
        if (p[i]==0 and q[i] < 0):
            print("line completely outside the window")
        else:
            if (p[i]==0 and q[i] >= 0):
                print("line completely inside the window")
if (t[0] > t[2]):
    t1=t[0]
    
else:
    t1=t[2]
    
if (t[1] < t[3]):
    t2=t[1]
else:
    t2=t[3]
    
if (t1 < t2):
    xx1=x1+t1*dx
    xx2=x1+t2*dx
    yy1=y1+t1*dy
    yy2=y1+t2*dy
    print("line after clipping:")
    l=Line(Point(xx1,yy1),Point(xx2,yy2))
    l.setFill("red")
    l.draw(win)


else:
    print("line lies out of the window")
 
try:
    win.getMouse()
except GraphicsError:
    pass
win.close()
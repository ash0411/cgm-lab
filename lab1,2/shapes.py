from graphics import *
# to draw a rectangle circle and a normal line
def shapes(x1,y1,x2,y2,r):
    win = GraphWin('shapes'))# here default width of 200 is used
    head = Circle(Point(x1,y1),r # making a circle
    rect = Rectangle(Point(x1,y1),Point(x2,y2))# making a rectangle
    line = Line(Point(x1,y1),Point(x2,y2))# making a line
    rect.draw(win)
    line.draw(win)
    head.draw(win)
    win.getMouse()
#help(Point)
shapes(10,20,50,60,10)
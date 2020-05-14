from graphics import *
from random import randint
def triangle():
    win = GraphWin("triangle")
    vertices = []
    for i in range(3):
        x = randint(0,200)
        y= randint(0,200)
        vertices.append(Point(x,y))
    triangle = Polygon(vertices)
    triangle.setFill("ORANGE")
    triangle.draw(win)
    win.getMouse()
triangle()
from graphics import *
from time import sleep

win = GraphWin("polygon",width=300,height=300)
#a1 = Polygon(Point(150,100),Point(50,150),Point(50,250),Point(250,250),Point(250,150))
#a1.setFill("blue")
#a1.setOutline("green")
a1 = Line(Point(150,100),Point(50,150))
a2 = Line(Point(50,150),Point(50,250))
a3 = Line(Point(50,250),Point(250,250))
a4 = Line(Point(250,250),Point(250,150))
a5 = Line(Point(250,150),Point(150,100))
a1.setOutline("red")
a2.setOutline("yellow")
a3.setOutline("red")
a4.setOutline("yellow")
a5.setOutline("blue")
a2.draw(win)
time.sleep(0.5)
a1.draw(win)
time.sleep(0.5)
a3.draw(win)
time.sleep(0.5)
a4.draw(win)
time.sleep(0.5)
a5.draw(win)

win.getKey()
 
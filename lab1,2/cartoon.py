from graphics import *
def cartoon():
    win = GraphWin("cartoon")
    cr = Circle(Point(55,30),20)# head
    cr.draw(win)
    cr_eL= Circle(Point(45,20),3)
    cr_eL.draw(win)
    cr_eR= Circle(Point(65,20),3)
    cr_eR.draw(win)
    mouth = Line(Point(60,45),Point(50,45))
    mouth.draw(win)
    ln1 = Line(Point(50,48),Point(50,66))
    ln1.draw(win)
    ln2 = Line(Point(60,48),Point(60,66))
    ln2.draw(win)
    rect = Rectangle(Point(40,66),Point(70,116))
    rect.draw(win)
    ln_h1 = Line(Point(70,76),Point(80,90))# right hand 1
    ln_h2 = Line(Point(80,90),Point(90,76))# right hand 2
    ln_h1.draw(win)
    ln_h2.draw(win)
    ln_h3 = Line(Point(40,76),Point(30,90))# left hand 1
    ln_h4 = Line(Point(30,90),Point(20,76))# left hand 2
    ln_h3.draw(win)
    ln_h4.draw(win)
    ln_l1 = Line(Point(50,116),Point(50,136))# left leg
    ln_l2 = Line(Point(60,116),Point(60,136))# right leg
    ln_l1.draw(win)
    ln_l2.draw(win)
    win.getMouse()
cartoon()
from time import sleep
from graphics import *
def flood_fill(win,x,y,old_color,new_color):
    p1 = Point(x,y)
    p1.draw(win)
    overlapping = win.find_overlapping(p1.x,p1.y,p1.x,p1.y)
    if overlapping:
        c = win.itemcget(overlapping[0],"fill")
        print(c)
        print("hey")
    print("outside the overlapping")
    print(new_color)
    if c == old_color:
        p1.setOutline(new_color)
        flood_fill(x + 1, y, old_color,new_color) 
        flood_fill(x - 1, y, old_color,new_color) 
        flood_fill(x, y + 1, old_color,new_color) 
        flood_fill(x, y - 1, old_color,new_color)
    #print("ended")
    win.getKey()
win = GraphWin("akansha",width=300,height=300)
road = Circle(Point(150, 150), 100)
road.setFill('pink')
road.draw(win)
flood_fill(win,150,150,"pink","blue")


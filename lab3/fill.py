from time import sleep
from graphics import *

paper = GraphWin(width=300, height=300)

road = Circle(Point(150, 150), 100)
road.setFill('pink')
road.draw(paper)

Line(Point(150, 50), Point(150, 0)).draw(paper)
Line(Point(50, 150), Point(0, 150)).draw(paper)
Line(Point(250, 150), Point(300, 150)).draw(paper)
Line(Point(150, 250), Point(150, 300)).draw(paper)

car = Circle(Point(0, 150), 5)
car.setFill('white')
car.draw(paper)

for _ in range(300):
    car.move(1, 0)

    center = car.getCenter()
    overlapping = paper.find_overlapping(center.x, center.y, center.x, center.y)
    if overlapping:
        print(paper.itemcget(overlapping[0], "fill"))

    sleep(0.05)
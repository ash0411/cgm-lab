# #! usr/bin/python
# from PIL import Image, ImageDraw
# import math

# # Set the starting shape
# img = Image.new('RGB', (1000, 1000))
# draw = ImageDraw.Draw(img)

# curve_X = [0, 0, 1, 1]
# curve_Y = [0, 1, 1, 0]

# combinedCurve = zip(curve_X, curve_Y)
# draw.line((combinedCurve), fill=(220, 255, 250))
# iterations = 5

# # Start the loop
# for i in range(0, iterations):
#     # Make 4 copies of the curve

#     copy1_X = list(curve_X)
#     copy1_Y = list(curve_Y)

#     copy2_X = list(curve_X)
#     copy2_Y = list(curve_Y)

#     copy3_X = list(curve_X)
#     copy3_Y = list(curve_Y)

#     copy4_X = list(curve_X)
#     copy4_Y = list(curve_Y)

#     # For copy 1, rotate it by 90 degree clockwise
#     # Then move it to the bottom left
#     # For copy 2, move it to the top left
#     # For copy 3, move it to the top right
#     # For copy 4, rotate it by 90 degrees anticlockwise
#     # Then move it to the bottom right

#     # Finally, combine all the copies into a big list
#     combinedCurve_X = copy1_X + copy2_X + copy3_X + copy4_X
#     combinedCurve_Y = copy1_Y + copy2_Y + copy3_Y + copy4_Y

# # Make the initial curve equal to the combined one
# curve_X = combinedCurve_X[:]
# curve_Y = combinedCurve_Y[:]

# # Repeat the loop

# # Scale it to fit the canvas
# curve_X = [x * xSize for x in curve_X]
# curve_Y = [y * ySize for y in curve_Y]
# # Draw it with something that connects the dots
# curveCoordinates = zip(curve_X, curve_Y)
# draw.line((curveCoordinates), fill=(255, 255, 255))

# img2=img.rotate(180)
# img2.show()'
from graphics import *
from math import sin,cos,radians
image_height = 1000
image_width = 1000

win = GraphWin( "2d transformation",image_height,image_width)
win.setBackground(color_rgb(255,255,255))
corners = [[100,100],[150,100],[150,150],[100,150]]
figure = Polygon(Point(corners[0][0],corners[0][1]),Point(corners[1][0],corners[1][1]),Point(corners[2][0],corners[2][1]),Point(corners[3][0],corners[3][1]))
figure.setOutline("red")
figure.draw(win)
# rotated polygon
corners_rotated = []
angle = 30
angle = radians(angle)
for x in range(4):
    corner_rotated = []
    corner = corners[x][0]*cos(angle)-corners[x][1]*sin(angle)
    corner_rotated.append(corner)
    corner = corners[x][0]*sin(angle)+corners[x][1]*cos(angle)
    corner_rotated.append(corner)
    corners_rotated.append(corner_rotated)
figure = Polygon(Point(corners_rotated[0][0],corners_rotated[0][1]),Point(corners_rotated[1][0],corners_rotated[1][1]),Point(corners_rotated[2][0],corners_rotated[2][1]),Point(corners_rotated[3][0],corners_rotated[3][1]))  
figure.setOutline("green")
figure.draw(win)
# translation polygon
corners_translated = []
tx = 30
ty = 40
angle = radians(angle)
for x in range(4):
    corner_translated = []
    corner = corners[x][0] + tx
    corner_translated.append(corner)
    corner = corners[x][1] +ty
    corner_translated.append(corner)
    corners_translated.append(corner_translated)
figure = Polygon(Point(corners_translated[0][0],corners_translated[0][1]),Point(corners_translated[1][0],corners_translated[1][1]),Point(corners_translated[2][0],corners_translated[2][1]),Point(corners_translated[3][0],corners_translated[3][1]))  
figure.setOutline("blue")
figure.draw(win)
# scaling polygon
corners_scaled = []
factor = 2
for x in range(4):
    corner_scaled = []
    corner = corners[x][0]*factor
    corner_scaled.append(corner)
    corner = corners[x][1]*factor
    corner_scaled.append(corner)
    corners_scaled.append(corner_scaled)
figure = Polygon(Point(corners_scaled[0][0],corners_scaled[0][1]),Point(corners_scaled[1][0],corners_scaled[1][1]),Point(corners_scaled[2][0],corners_scaled[2][1]),Point(corners_scaled[3][0],corners_scaled[3][1]))  
figure.setOutline("black")
figure.draw(win)
try:
    win.getMouse()
except GraphicsError :
    pass
win.close()  
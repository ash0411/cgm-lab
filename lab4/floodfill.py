from PIL import Image, ImageDraw
import random
import sys
sys.setrecursionlimit(50000)

im = Image.new('RGB', (500, 500), (128, 128, 128))
draw = ImageDraw.Draw(im)

#draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.polygon((250,100,250+100,200,250+100,300,250-100,300,250-100,200))

def flood_fill(x,y,previous_color,new_color):

	if (im.getpixel((x,y)) != previous_color):
		return

	im.putpixel((x,y),new_color)

	flood_fill(x + 1, y, previous_color, new_color)
	flood_fill(x, y + 1, previous_color, new_color)
	flood_fill(x - 1, y, previous_color, new_color)
	flood_fill(x, y - 1, previous_color, new_color)

flood_fill(250,250,(128,128,128),(255,255,255))

im.show()
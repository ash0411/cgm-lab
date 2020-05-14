from PIL import Image, ImageDraw
import random
import sys
sys.setrecursionlimit(30000)

im = Image.new('RGB', (500, 500), (128, 128, 128))
draw = ImageDraw.Draw(im)

#draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.polygon((250,100,250+100,200,250+100,300,250-100,300,250-100,200),outline = (128,255,255))

def boundary_fill(x,y,fill_color,boundary_color):
	if (im.getpixel((x,y)) != fill_color and im.getpixel((x,y)) != boundary_color):

		im.putpixel((x,y),fill_color)

		boundary_fill(x + 1, y, fill_color, boundary_color)
		boundary_fill(x, y + 1, fill_color, boundary_color)
		boundary_fill(x - 1, y, fill_color, boundary_color)
		boundary_fill(x, y - 1, fill_color, boundary_color)

boundary_fill(250,250,(128,128,255),(128,255,255))

im.show()
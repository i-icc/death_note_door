#!/usr/bin/python
# -*- coding:utf-8 -*-

import spidev as SPI
import ST7789
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0 
device = 0 

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
disp.Init()

# Clear display.
disp.clear()

# Create blank image for drawing.
image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(image1)
font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 30)
font10 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',15)
draw.line([(40,20),(200,20)], fill = "BLUE",width = 5)
draw.line([(40,20),(40,200)], fill = "BLUE",width = 5)
draw.line([(40,200),(200,200)], fill = "BLUE",width = 5)
draw.line([(200,20),(200,200)], fill = "BLUE",width = 5)
#print "***draw rectangle"
print("Python3 test")
draw.rectangle([(50,30),(190,70)],fill = "BLUE")
disp.ShowImage(image1,0,0)
time.sleep(3)

draw.text((60,30), u'微雪电子 ', font = font, fill = "WHITE")
draw.text((50, 75), 'Waveshare Electronic ', font = font10, fill = "BLUE")
draw.text((75, 110), '1.3inch LCD ', font = font10, fill = "BLUE")
draw.text((72, 140), 'Test Program ', font = font10, fill = "BLUE")
#image1=image1.rotate(45) 
disp.ShowImage(image1,0,0)
time.sleep(3)

image = Image.open('pic.jpg')	
disp.ShowImage(image,0,0)



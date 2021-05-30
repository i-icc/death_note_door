import time
import seeed_dht
import spidev as SPI
import ST7789

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

def main():
    RST = 27
    DC = 25
    BL = 24
    bus = 0 
    device = 0 

    disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)
    disp.Init()
    disp.clear()

    font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 30)

    sensor = seeed_dht.DHT("22", 12)
    
    while True:
        image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        humi, temp = sensor.read()
        if not humi is None:
            draw.text((68, 140), f"temp:{temp:.1f}°C\nhumi:{humi:.1f}%", font = font, fill = "BLUE")
            disp.ShowImage(image1,0,0)
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        time.sleep(1)


if __name__ == '__main__':
    main()

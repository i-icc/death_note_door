import time
import RPi.GPIO as GPIO
import atexit
import MySQLdb
import seeed_dht
import spidev as SPI
import ST7789

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

GPIO.setmode(GPIO.BCM)
conn = MySQLdb.connect(
user='i-icc',
passwd='',
host='localhost',
db='door_log')
cur = conn.cursor()

class Door:
    def __init__(self, in_n):
        self.is_open = False
        self.was_open = False
        self.in_n = in_n

        GPIO.setup(in_n, GPIO.IN)

    def update(self):
        self.is_open = 0 if GPIO.input(self.in_n) == 1 else 1 # 更新　ドア情報を取る関数作る
        result = self.is_open != self.was_open
        self.was_open = self.is_open
        return [result, self.is_open]

class Disp:
    def __init__(self):
        self.RST = 27
        self.DC = 25
        self.BL = 24
        self.bus = 0 
        self.device = 0 
        self.disp = ST7789.ST7789(SPI.SpiDev(self.bus, self.device),self.RST, self.DC, self.BL)
        self.disp.Init()
        self.disp.clear()
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 30)
        self.font2 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 60)

    def draw(self,is_open,humi,temp):
        image1 = Image.new("RGB", (self.disp.width, self.disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        if is_open:
            draw.text((30, 30), "OPEN", font = self.font2, fill = "BLUE")
        else:
            draw.text((30, 30), "CLOSE", font = self.font2, fill = "BLUE")
        if not humi is None:
            draw.text((30, 140), f"temp:{temp:.1f}°C\nhumi:{humi:.1f}%", font = self.font, fill = "BLUE")
        self.disp.ShowImage(image1,0,0)

def observe():
    print('Observe Start')
    door = Door(17)
    disp = Disp()
    sensor = seeed_dht.DHT("22", 12)
    while True:
        result = door.update()
        humi, temp = sensor.read()
        sql = f"INSERT INTO temp_record(humi,temp) VALUES (humi,temp);"
        cur.execute(sql)
        if result[0]:
            sql = f"INSERT INTO door_record(is_open) VALUES ('{result[1]}');"
            cur.execute(sql)
        try:
            disp.draw(result[1],humi,temp)
            time.sleep(0.5)
            conn.commit()
        except KeyboardInterrupt:
            pass

def main():
    observe()

def atExit():
    print('Observe Finish')
    print("atExit")
    GPIO.cleanup()
    conn.close()
    cur.close()

if __name__ == '__main__':
    atexit.register(atExit)
    main()

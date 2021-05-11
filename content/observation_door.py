import time
import RPi.GPIO as GPIO
import atexit
import MySQLdb

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
        self.is_open = GPIO.input(self.in_n) # 更新　ドア情報を取る関数作る
        result = self.is_open != self.was_open
        self.was_open = self.is_open
        return [result, self.is_open]

def observe():
    print('Observe Start')
    door = Door(17)
    while True:
        result = door.update()
        if result[0]:
            sql = f"INSERT INTO door_record(is_open) VALUES ('{result[1]}');"
            cur.execute(sql)
            conn.commit()
            print(sql)
        time.sleep(1)

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

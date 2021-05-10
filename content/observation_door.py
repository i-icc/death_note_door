import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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
    door = Door(12)
    while True:
        result = door.update()
        if result[0]:
            pass
        time.sleep(1)
        print("a")

def atExit():
    print("atExit")
    GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(atExit)
    main()

import time

class Door:
    def __init__(self):
        self.is_open = False
        self.was_open = False

    def update(self):
        self.is_open = False # 更新　ドア情報を取る関数作る
        self.was_open = self.is_open
        return [self.is_open != self.was_open, self.is_open]

def observe():
    print('Observe Start')
    door = Door()
    while True:
        result = door.update()
        if result[0]:
            pass
        time.sleep(1)
        print("a")

def main():
    observe()

if __name__ == '__main__':
    main()

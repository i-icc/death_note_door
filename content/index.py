# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
# import RPi.GPIO as GPIO
import atexit
import datetime

class Door:
    def __init__(self):
        self.is_open = False
        self.was_open = False

    def update(self):
        self.is_open = False # 更新　ドア情報を取る関数作る
        self.was_open = self.is_open
        return [self.is_open != self.was_open, self.is_open]

# ピン情報等々　初期値
door = Door()

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

# curl http://192.168.1.16:8080/getR
@route('/getJson', method='GET')
def getJson():
    retBody = {
        "ret": "ok",
        "r": 1,
        "val": 1,
    }
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r

# curl http://192.168.1.16:8080/getDoor
@route('/getDoor', method='GET')
def getDoor():
    global door
    result = door.update()
    retBody = {
        "is_open": result[1],
        "change": result[0],
    }
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r

def main():
    print('Server Start')
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
    print("atExit")
    # GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(atExit)
    main()

# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import RPi.GPIO as GPIO
import atexit
import MySQLdb
import json

conn = MySQLdb.connect(
user = 'i-icc',
password = '',
host = 'localhost'
db = 'door_log')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

# curl http://192.168.1.16:8080/getR
@route('/getJson', method='GET')
def getJson(n):
    retBody = {
        "ret": "ok",
        "r": 1,
        "val": 1,
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

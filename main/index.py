# coding: utf-8
from flask import *
import json
import atexit
import MySQLdb
import json
import os

from datetime import datetime, date, timedelta

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError("Type %s not serializable" % type(obj))

app = Flask(__name__)

@app.route('/')
def root():
    r = json.loads(getJsonDoor(1))
    is_open = r["log"][0]["is_open"]
    rr = json.loads(getJsonTemp(1))
    temp = rr["log"][0]["temp"]
    humi = rr["log"][0]["humi"]
    return render_template("index.html",is_open=is_open,temp=temp,humi=humi)

@app.route('/door_log/')
def door_log():
    n = request.args.get('n')
    n = 5 if n is None else int(n)
    r = json.loads(getJsonDoor(n))
    return render_template("door.html",req=r)

@app.route('/temp_log')
def temp_log():
    n = request.args.get('n')
    n = 5 if n is None else int(n)
    r = json.loads(getJsonTemp(n))
    return render_template("temp.html",req=r)

@app.route('/getJsonDoor')
def getJsonDoor(n):
    conn = MySQLdb.connect(
    user = 'i-icc',
    password = '',
    host = 'localhost',
    db = 'door_log')
    n = request.args.get('n')
    n = 5 if n is None else int(n)
    sql = f"SELECT * FROM door_record ORDER BY id DESC LIMIT {n};"
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    res = {}
    res["log"] = data
    res["status"] = "200"
    r = json.dumps(res, default=json_serial)
    conn.close()
    return r

@app.route('/getJsonTemp')
def getJsonTemp(n):
    conn = MySQLdb.connect(
    user = 'i-icc',
    password = '',
    host = 'localhost',
    db = 'door_log')
    n = request.args.get('n')
    n = 5 if n is None else int(n)
    sql = f"SELECT * FROM temp_record ORDER BY id DESC LIMIT {n};"
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    res = {}
    res["log"] = data
    res["status"] = "200"
    r = json.dumps(res, default=json_serial)
    conn.close()
    return r

def main():
    print('Server Start')
    app.run(host='0.0.0.0',debug=True)
    #app.run(host='192.168.1.1',debug=True)

def atExit():
    print("atExit")

if __name__ == '__main__':
    atexit.register(atExit)
    main()

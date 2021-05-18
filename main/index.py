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

conn = MySQLdb.connect(
user = 'i-icc',
password = '',
host = 'localhost',
db = 'door_log')

app = Flask(__name__)

@app.route('/')
def root():
    #n = request.query.get('n')
    #n = 5 if n is None else int(n)
    n = 5
    r = json.loads(getJson())
    #r = getJson(n)
    return r
    # return template("index",req=r)
    #  return "<html><body>hello</body></html>"

# curl http://192.168.1.16:8080/getR
@app.route('/getJson')
def getJson(n = 5):
    #n = request.query.get('n')
    n = 5 if n is None else int(n)
    sql = f"SELECT * FROM door_record ORDER BY id DESC LIMIT {n};"
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    res = {}
    res["log"] = data
    res["status"] = "200"
    r = json.dumps(res, default=json_serial)
    # r = HTTPResponse(status=200, body=retBody)
    # r.set_header('Content-Type', 'application/json')
    return r

def main():
    print('Server Start')
    app.run(debug=True)

def atExit():
    print("atExit")
    conn.close()

if __name__ == '__main__':
    atexit.register(atExit)
    main()

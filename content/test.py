import MySQLdb
import json
from datetime import datetime, date, timedelta

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError("Type %s not serializable" % type(obj))

conn = MySQLdb.connect(
user='i-icc',
password='',
host='localhost',
db='door_log'
)

sql = 'SELECT * FROM door_record ORDER BY id DESC LIMIT 5;'
cur = conn.cursor(MySQLdb.cursors.DictCursor)
cur.execute(sql)
data = cur.fetchall()
conn.close()
res = {}
res["log"] = data
res["status"] = "200"


print(json.dumps(res, default=json_serial))

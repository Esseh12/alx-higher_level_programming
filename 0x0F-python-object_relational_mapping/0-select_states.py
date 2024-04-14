#!/usr/bin/python3

import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="Ese", passwd="root", db="my_db", charset="utf8")

cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

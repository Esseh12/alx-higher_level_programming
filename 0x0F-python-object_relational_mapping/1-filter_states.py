#!/usr/bin/python3

"""a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

curr = db.cursor()
curr.execute("SELECT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

rows = curr.fetchall()
for row in rows:
    print(row)
curr.close()
db.close()

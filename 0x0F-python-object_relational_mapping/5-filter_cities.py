#!/usr/bin/python3

""" a script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    cur.close()
    db.close()

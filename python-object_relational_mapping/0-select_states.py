#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

db = MySQLdb.connect(host=localhost, port=3306, user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
c = db.cursor()

query = "SELECT * FROM states ORDER BY states.id"
c.execute(query)

rows = c.fetchall()
for row in rows:
    print(row)
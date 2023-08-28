#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

""" To not execute when imported """
if __name__ == '__main__':

    """ Make a connection with the database """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    """ Creating cursor """
    c = db.cursor()

    """ Execute queries """
    query = "SELECT * FROM cities ORDER BY id"
    c.execute(query)

    """ Printing all the rows """
    rows = c.fetchall()
    for row in rows:
        print(row)

    """ Cleaning process """
    c.close()
    db.close()

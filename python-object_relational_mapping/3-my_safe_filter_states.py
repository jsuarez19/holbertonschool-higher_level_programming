#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    c.execute(query, (sys.argv[4],))

    """ Printing all the rows """
    rows = c.fetchall()
    for row in rows:
        print(row)
        
    """ Cleaning process """
    c.close()
    db.close()

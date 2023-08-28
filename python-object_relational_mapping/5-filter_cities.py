#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
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
    query = "SELECT cities.name \
FROM cities \
INNER JOIN states \
ON states.id = cities.state_id \
WHERE states.name = %s \
ORDER BY cities.id"
    c.execute(query, (sys.argv[4],))

    """ Printing all the rows """
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    print(", ".join(result))

    """ Cleaning process """
    c.close()
    db.close()

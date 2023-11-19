#!/usr/bin/python3
import MySQLdb
import sys

""" Write a script that lists all states from the database hbtn_0e_0_usa"""
""" code should not be executed when imported"""
if __name__ == "__main__":
    """ script should take 3 arguments: mysql username, mysql password """
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    """ Results must be sorted in ascending order by states.id """
    """ execute query """
    cur.execute("SELECT * FROM states WHERE\
    name LIKE BINARY 'N%' ORDER BY states.id")

    """ fetch and print """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ close cursor and database"""
    cur.close()
    db.close()

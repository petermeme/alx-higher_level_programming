#!/usr/bin/python3
import MySQLdb
import sys

# Write a script that lists all states from the database hbtn_0e_0_usa
# code should not be executed when imported
if __name__ == "__main__":
    # script should take 3 arguments: mysql username, mysql password
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # Results must be sorted in ascending order by states.id
    cur.execute("SELECT * FROM states WHERE BINARY name = '{:s}'\
    ORDER BY id ASC".format(sys.argv[4]))
    [print (state) for state in cur.fetchall()]

    cur.close()
    db.close()

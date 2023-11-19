#!/usr/bin/python3
import MySQLdb
import sys

#Write a script that lists all states from the database hbtn_0e_0_usa
#code should not be executed when imported
if __name__ == "__main__":
    #script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    #Results must be sorted in ascending order by states.id
    cur.execute("SELECT * FROM states ORDER BY id")
    [print (state) for state in cur.fetchall()]

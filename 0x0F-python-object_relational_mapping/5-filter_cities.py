#!/usr/bin/python3
import MySQLdb
from sys import argv

#Write a script that lists all states from the database hbtn_0e_0_usa
#code should not be executed when imported
if __name__ == "__main__":
    #script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    db = MySQLdb.connect(host='localhost',port=3306,user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    #Results must be sorted in ascending order by states.id
    state = (argv[4], )
    cmd = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id AND states.name = %s ORDER BY cities.id ASC"

    cur.execute(cmd, state)

    # fetch
    rows = cur.fetchall()

    # print
    ll = [x[0] for x in rows]
    together = ", ".join(ll)
    print(together)

    # close
    cur.close()
    db.close()

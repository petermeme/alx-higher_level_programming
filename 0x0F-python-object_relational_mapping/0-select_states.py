#!/usr/bin/python3
import MySQLdb
from sys import argv

# Write a script that lists all states from the database hbtn_0e_0_usa
# code should not be executed when imported
if __name__ == "__main__":
    # script should take 3 arguments: mysql username, mysql password
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    cur = db.cursor()
    # Results must be sorted in ascending order by states.id
    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()
    for record in results:
        print(record)

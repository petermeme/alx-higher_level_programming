#!/usr/bin/python3
"""
This module  lists all states from the database hbtn_0e_0_usa
starting with N
"""
import sys

import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         password=password, db=database, charset='utf8')
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states
    WHERE BINARY name LIKE 'N%' ORDER BY id ASC""")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()

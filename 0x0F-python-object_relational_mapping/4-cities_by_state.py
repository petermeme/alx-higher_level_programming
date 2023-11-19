#!/usr/bin/python3
"""This module  lists all cities from the database hbtn_0e_0_usa"""
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
    cur.execute("""SELECT ct.id, ct.name, st.name FROM cities ct JOIN
    states st ON st.id = ct.state_id ORDER BY id ASC""")
    for city in cur.fetchall():
        print(city)
    cur.close()
    db.close()

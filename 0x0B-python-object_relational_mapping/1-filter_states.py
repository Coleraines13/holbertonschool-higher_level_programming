#!/usr/bin/python3
"""this lists all states with names that start with a uppercase n"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        host='localhost',
                        port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
             FROM states
             WHERE name LIKE BINARY 'N%'
             ORDER BY id ASC;"""
    cur = db.cursor()
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()

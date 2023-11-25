#!/usr/bin/python3
"""
Module that list all the states with name starting with N
from hbtn_0e_0_usa database.
"""

import MySQLdb
import sys

if __name__ = "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
    
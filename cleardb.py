#!/usr/bin/python
import sqlite3 as lite

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("DELETE FROM trades")
raw_input("DB Empty press any key to close")
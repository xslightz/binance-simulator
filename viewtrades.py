#!/usr/bin/python

from colorama import init
init()
from colorama import Fore, Back, Style
import sqlite3 as lite


con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trades")
    rows = cur.fetchall()

    for row in rows:
        print Fore.LIGHTMAGENTA_EX + "Pair: " + Fore.LIGHTWHITE_EX + row[1] + Fore.LIGHTMAGENTA_EX + " Buy Price: " + Fore.LIGHTWHITE_EX + str(row[2]) + Fore.LIGHTMAGENTA_EX + " Goal: " + Fore.LIGHTWHITE_EX + str(row[3]) + Fore.LIGHTMAGENTA_EX +" Date: " + Fore.LIGHTWHITE_EX + str(row[4])

raw_input("pree any key to close")
#/usr/bin/python
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
import settings
import sqlite3 as lite
import sys
import time

from binance.client import Client
client = Client(settings.api_key, settings.api_secret)
from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
pairs = raw_input("Type the pair e.g BNBBTC: ")
pairs = pairs.upper()
tickers = client.get_ticker(symbol=pairs)
str2 = tickers['lastPrice']
str2 = str2.replace(".", "")
str2 = str2.lstrip("0")
lastp = int(str2)
con = lite.connect('test.db')
time = time.asctime( time.localtime(time.time()) )

def calculate(x, y):
    z = (x * y)
    final = x + z
    return final

a = round(calculate(lastp, 0.01)) #0.01 for 1% gain
a=int(a)

q = "INSERT INTO `trades`(`id`,`pair`,`buy`,`goal`,`time`) VALUES (NULL,'"+ pairs +"','"+str(lastp)+"','"+str(a)+"','"+time+"')"

with con:
    cur = con.cursor()
    cur.execute(q)

    lid = cur.lastrowid
    cur.execute("SELECT * FROM trades WHERE Id=:Id",
                {"Id": lid})
    con.commit()
    row = cur.fetchone()
    pair = row[1]
    price = row[2]
    goal = row[3]
    print "Trading Simulator" + Fore.LIGHTGREEN_EX + " Started" + Style.RESET_ALL

def process_message(msg):

    mprice = msg['c']
    mprice = mprice.replace(".", "")
    mprice = mprice.lstrip("0")
    mprice = int(mprice)

    if (mprice) > a:
        print Back.GREEN + Fore.LIGHTWHITE_EX + "Pair: " + pair, "Last Price:", mprice, "Goal:", goal
    else:
        print Fore.LIGHTMAGENTA_EX + "Pair: " + Fore.LIGHTWHITE_EX, pair, Fore.LIGHTMAGENTA_EX + "Last Price:" + Fore.LIGHTWHITE_EX, mprice, Fore.LIGHTMAGENTA_EX, "Goal:", Fore.LIGHTWHITE_EX, goal

conn_key = bm.start_symbol_ticker_socket(pair, process_message)
bm.start()

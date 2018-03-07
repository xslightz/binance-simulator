# Binance Simulator

I created this simulator in the hopes I can test the signals without actually spending any coins. Obviously, if the signal was good you won’t earn money same as if it was bad you won’t lose. I’ve set a 1% profit to test if the signal was worth it and decide to buy or not. You can change the percentage on line 30 change 0.01 to whatever you want 0.01 equals 1% the code is not “professional” as I did this for myself just thought I’d share perhaps it might be useful to someone as well.

## Configuration

1. Signup Binance ( Referral url: https://www.binance.com/?ref=23209789 )
2. Enable Two-factor Authentication    
3. Go API Center, https://www.binance.com/userCenter/createApi.html
4. Create New Key

        [✓] Read Info [X] Enable Trading [X] Enable Withdrawals 
5. Open settings.py
6. Get an API and Secret Key, insert into config.py

        API key for account access
        api_key = ''
        Secret key for account access
        api_secret = ''

        API Docs: https://www.binance.com/restapipub.html

## Requirements

    sudo easy_install -U colorama python-binance
    or 
    sudo pip install colorama python-binance
    
    Python 2.7
        import colorama
        import time
        import settings
        import binance
        import sqlite3


## Usage

    python simulator.py

type the pair you want for example xvgbtc
currently its set to 1% gain, it can be changed in the settings.py just increase the decimal from 0.01 to a number you want.
note: for 3% is 0.03 and so.


type the pairs you want and wait.

![simulator](http://excdn.pw/binance.png)

## Files

viewtrades.py list all trades iin the database

cleardb.py WARNING this empty the database from all records

simulator.py Main file to start the simulator, you can enter the pairs in lowercase or uppercase.

## Contributing
The code can be improved so any contributions are highly appreciated im always looking to learn new ways to do things.

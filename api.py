import requests
import sqlite3 as lite

def key_word(key):
    con = lite.connect('/var/www/FlaskApp/FlaskApp/DataBase.db')
    with con:
        cur = con.cursor()
        url='https://api.cryptonator.com/api/ticker/'
        url+= key
        respond=requests.get(url).json()
        currency= respond['ticker']
        price= currency['price']
        name= currency['base']
        cur.execute("SELECT Price from items WHERE Name=?",(name,))
        p=cur.fetchone()
        change=0
        old=p[0]
        if price>old:
            x=float(price)-old
        else:
            x=old-float(price)
        change=(x/old)*100
        cur.execute('''UPDATE items SET Price=?,Change=? WHERE Name =?''',(price,change,name))
        con.commit()
x=[]
x.append('btc-usd')
x.append('xrp-usd')
x.append('neo-usd')
x.append('eth-usd')
def run():
    for n in x:
        key_word(n)


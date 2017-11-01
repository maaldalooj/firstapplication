from flask import Flask,render_template
from api import run
import sqlite3 as sql
import time
import os
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("home.html")
    #return "Hello World"
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

@app.route("/data")
def data():
    run()
    con = sql.connect("/var/www/FlaskApp/FlaskApp/DataBase.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from items")
    rows = cur.fetchall(); 
    return render_template("data.html",rows = rows)
if __name__ == "__main__":
    app.run(debug=True)

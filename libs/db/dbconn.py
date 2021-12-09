
import sqlite3

def getconn():
    conn = sqlite3.connect('c:/pydb/mydb.db')
    return conn

def dbconn(dbpath):
    conn = sqlite3.connect(dbpath)
    return conn

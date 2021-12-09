import cx_Oracle
import os

def getconn():
    LOCATION = r'c:/instantclient_19_12'
    os.environ["PATH"] = LOCATION + ":" + os.environ["PATH"] # 환경 설정
    conn = cx_Oracle.connect("system", "12345", "localhost:1522/xe")
    return conn

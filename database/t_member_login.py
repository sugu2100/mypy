from getpass import getpass
import sqlite3

def login():
    memberId = input("아이디 : ")
    #passwd = input("패스워드 : ")
    passwd = getpass("패스워드 : ")

    conn =  sqlite3.connect('c:/pydb/mydb.db')
    cur = conn.cursor()
    sql = "SELECT memberId, passwd FROM member"
    cur.execute(sql)
    rs = cur.fetchall()

    access = False   # 로그인 성공 여부
    for i in rs:
        if memberId == i[0] and passwd == i[1]:
            print("로그인에 성공했습니다.")
            access = True
            break
    if access == False:
        print("아이디나 비밀번호가 일치하지 않습니다.")
    conn.close()

login()


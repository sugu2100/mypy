import sqlite3

def login():
    eid = input("아이디 입력 : ")
    ename = input("이름 입력 : ")

    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "SELECT emp_id, name, age, salary  FROM employee"
    cur.execute(sql)
    rs = cur.fetchall()
    #print(rs)
    access = False   # 로그인 성공 여부
    for i in rs:
        if eid == i[0] and ename == i[1]:
            print("로그인에 성공했습니다.")
            access = True
            break
    if access == False:
        print("아이디나 비밀번호가 일치하지 않습니다.")
    conn.close()

login()
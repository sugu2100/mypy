#from libs.db.dbconn import getconn
import sqlite3

def select_emp():
    #conn = getconn()
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "select * from employee order by emp_id"
    cur.execute(sql)
    rs = cur.fetchall()   # rs=resultSet의 약자
    for i in rs:
        print(i)
    conn.close()

def select_one():
    #conn = getconn()
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e101',))  # 튜플은 1개일때 코머를 꼭 붙인다.
    rs = cur.fetchone()
    print(rs)
    conn.close()

def insert_emp():
    #conn = getconn()
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?, ?, ?, ?)"
    cur.execute(sql, ('e201', '장그래', 27, 10000))
    conn.commit()
    conn.close()

def update_emp():
    #conn = getconn()
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "update employee set salary=? where emp_id=?"
    #추신수의 급여를 10000에서 30000으로 변경
    cur.execute(sql, (30000, 'e101'))
    conn.commit()
    conn.close()

def delete_emp():
    #conn = getconn()
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    # 사원 아이디가 'e102'인 사원 정보를 삭제
    sql = "delete from employee where emp_id=?"
    cur.execute(sql, ('e201', ))
    conn.commit()
    conn.close()

if __name__=="__main__":
    #insert_emp()
    #update_emp()
    #delete_emp()
    select_emp()
    #select_one()

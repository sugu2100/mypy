from libs.db.dbconn import getconn

def select_dept():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from department"
    cur.execute(sql)
    rs = cur.fetchall()   # rs=resultSet의 약자
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e102',))  # 튜플은 1개일때 코머를 꼭 붙인다.
    rs = cur.fetchone()
    print(rs)
    conn.close()

def insert_dept():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into department(dname, dtel, location) values (?, ?, ?)"
    cur.execute(sql, ('기계공학과', '032-456-4567', 'B동 1층'))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set salary=? where emp_id=?"
    #추신수의 급여를 10000에서 30000으로 변경
    cur.execute(sql, (30000, 'e102'))
    conn.commit()
    conn.close()

def delete_dept():
    conn = getconn()
    cur = conn.cursor()
    # 사원 아이디가 'e102'인 사원 정보를 삭제
    sql = "delete from department where dname=?"
    cur.execute(sql, ('생명공학과', ))
    conn.commit()
    conn.close()

if __name__=="__main__":
    #insert_dept()
    #delete_dept()
    select_dept()

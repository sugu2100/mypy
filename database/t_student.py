from libs.db.dbconn import getconn

def select_std():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from student"
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

def insert_std():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into student(snum, name, age, gender, dname) values (?, ?, ?, ?, ?)"
    cur.execute(sql, (1005, '황진이', 31, '여자', '생명공학과'))
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

def delete_std():
    conn = getconn()
    cur = conn.cursor()
    # 사원 아이디가 'e102'인 사원 정보를 삭제
    sql = "delete from student where snum=?"
    cur.execute(sql, (1005, ))
    conn.commit()
    conn.close()

if __name__=="__main__":
    #insert_std()
    #delete_std()
    select_std()

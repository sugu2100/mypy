from libs.db.dbconn import getconn
import sqlite3

# 테이블 만들기
def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member(
            memberId CHAR(5) PRIMARY KEY,
            passwd   CHAR(8) NOT NULL,
            name     TEXT NOT NULL,
            age      INTEGER,
            regDate  DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()

# 데이터 추가
def insert_member():
    conn = getconn()
    cur = conn.cursor()
    #추가 방법 1 - ? 기호로 대입(동적 입력)
    #sql = "INSERT INTO member(memberId, passwd, name, age) VALUES (?, ?, ?, ?)"
    #cur.execute(sql, ('1001', 'a1234567', '콩쥐', 17))
    #추가 방법 2 - 각 행의 레코드를 직접 입력
    sql = "INSERT INTO member(memberId, passwd, name, age) VALUES ('1002', 'b1234567', '팥쥐', 18 )"
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT memberId, passwd FROM member WHERE memberId = ?"
    cur.execute(sql, ('1002', ))
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET age = ? WHERE memberId = ?"
    cur.execute(sql, (19, '1002'))
    conn.commit()
    conn.close()

def delete_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberId = ?"
    cur.execute(sql, ('1003',))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #create_table()
    #insert_member()
    update_member()
    #delete_member()
    #select_one()
    select_member()




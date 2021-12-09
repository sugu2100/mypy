import sqlite3

def getconn():  # 데이터베이스 연결
    conn = sqlite3.connect('./output/test.db')
    return conn

def create_table():  # book 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        publisher TEXT NOT NULL,
        page INTEGER
    )
    """
    cur.execute(sql)
    print("book 테이블 생성")
    conn.commit()
    conn.close()

def insert_book():   # 책 추가 입력
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO book(title, publisher, page) VALUES (?, ?, ?)"
    cur.execute(sql, ('점프 투 파이썬', '박응용', 350))
    conn.commit()
    conn.close()

def select_book():  # 책 목록 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    rs = cur.fetchall()   # rs=resultSet의 약자
    for i in rs:
        print(i)
    conn.close()

def select_one():  # 특정한 책 검색
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no=?"
    cur.execute(sql, (2,))  # 튜플은 1개일때 코머를 꼭 붙인다.
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_book():  # 책 정보 변경
    conn = getconn()
    cur = conn.cursor()
    # 1번 책의 페이지를 600 -> 650으로 변경
    sql = "UPDATE book SET page=? WHERE book_no=?"
    cur.execute(sql, (650, 1))
    conn.commit()
    conn.close()

def delete_book():  # 책 삭제
    conn = getconn()
    cur = conn.cursor()
    # 2번책 삭제
    sql = "DELETE FROM book WHERE book_no=?"
    cur.execute(sql, (2,))
    conn.commit()
    conn.close()

if __name__=="__main__":
    #create_table()
    insert_book()
    select_book()
    # update_book()
    # delete_book()
    #select_one()


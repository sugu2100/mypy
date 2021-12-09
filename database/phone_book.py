import sqlite3
from libs.db.dbconn import dbconn

class PhoneBook:
    conn = dbconn("c:/pydb/willdb.db")
    cur = conn.cursor()

    def createtable(self):
        PhoneBook.cur.execute('CREATE TABLE phone(name TEXT, pno TEXT)')

    def insert(self):
        self.name = input('이름 : ')
        self.pno = input('전화번호 : ')
        self.sql = 'INSERT INTO phone VALUES (?, ?)'
        PhoneBook.cur.execute(self.sql, (self.name, self.pno))
        PhoneBook.conn.commit()

    def select(self):
        self.sql = 'SELECT * FROM phone'
        PhoneBook.cur.execute(self.sql)
        rs = PhoneBook.cur.fetchall()
        print("***** 전화 목록 ********")
        for i in rs:
            print(i)

    def delete(self):
        self.name = input('이름 : ')
        self.sql = "DELETE FROM phone WHERE name = ?"
        PhoneBook.cur.execute(self.sql, (self.name, ))
        PhoneBook.conn.commit()

def main():
    pb = PhoneBook()
    while True:
        n = input("a.테이블 생성 | 1.입력 | 2.조회 | 3.삭제 | 4.수정 | 0.종료\n선택> ")
        if n == 'a':
            pb.createtable()
        if n == '1':
            pb.insert()
        if n == '2':
            pb.select()
        if n == '3':
            pb.delete()
        if n == '0':
            pb.conn.close()

main()
import sqlite3

conn = sqlite3.connect("./output/sample.db")
cur = conn.cursor()

# 테이블 생성
sql = '''
CREATE TABLE product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price INTEGER,
    link TEXT
)
'''
cur.execute(sql)
conn.commit()

conn.close()
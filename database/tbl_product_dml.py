import sqlite3

def get_conn():
    conn = sqlite3.connect("./output/sample.db")
    return conn

def insert():
    conn = get_conn()
    cur = conn.cursor()
    # 추가 방법1
    #sql = "INSERT INTO product(title, price, link) VALUES ('향수', 10000, '/product1.html')"
    # 추가 방법2
    #sql = "INSERT INTO product(title, price, link) VALUES (?, ?, ?)"
    #cur.execute(sql, ('손수건', 5000, '/product2.html'))

    #추가 방법3 - executemany()
    sql = "INSERT INTO product(title, price, link) VALUES (?, ?, ?)"
    data = (
        ("스웨터", 30000, '/product3.html'),
        ("바지", 25000, '/product4.html')
    )
    cur.executemany(sql, data)
    conn.commit()
    conn.close()

def select_all():
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM product"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()


insert()
select_all()

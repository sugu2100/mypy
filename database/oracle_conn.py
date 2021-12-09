from libs.db.oracle_dbconn import getconn

def select_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM person"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()

def insert_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO person VALUES ('park', 'p1234567', '박대양', 45)"
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
    select_data()



import pymysql

def mysql_db():
    # conn = mysql.connector.connect(user='root', password='pmv59-yk_hjoe49y-jfs3', host='localhost', database='test')
    db = pymysql.connect(user='root', password='pmv59-yk_hjoe49y-jfs3', host='localhost', db='test', charset='utf-8')
    # Dict形式で出力
    # cur = conn.cursor(pymysql.cursors.DictCursor)
    cur = db.cursor()
    yield cur

    cur.close()
    db.close()

if __name__ == '__main__':
    print("error")

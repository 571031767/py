# -*- coding: utf-8 -*-
import  pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"hanyu12345???",
    "database":"test"
}
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# sql = "INSERT INTO cmstop_api (name,sort)  VALUES(%s,%s)"
# result = cursor.execute(sql,("tom",12))

sql = "SELECT * from test"
cursor.execute(sql)
result = cursor.fetchall()

# result = cursor.executemany(sql,[("tom","123"),("alex",'321')])

cursor.close()
db.close()
if result:
    print(result)
else:
    print('登录失败')
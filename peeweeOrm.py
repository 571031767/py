# -*- coding: utf-8 -*-
from peewee import *
db ={
    "host":"127.0.0.1",
    "user":"root",
    "password":"hanyu12345???",
    "database":"test"
}

# connect database
database = MySQLDatabase("test",user = "root" ,password = "hanyu12345???" ,host ="127.0.0.1",port = 3306)
class Test(Model):
    type = CharField()
    name = CharField()
    id = IntegerField()

    class Meta:
        database = database

# Test.create_table() #新建数据
p = Test(type=1,name="wangbo")
# p.save(); 新增

# 教程参考https://www.jianshu.com/p/8d1bdd7f4ff5
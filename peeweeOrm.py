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
class Link(Model):
    id = IntegerField()
    name = CharField()
    img = CharField()
    url = CharField()
    ordid = IntegerField()
    status = IntegerField()

    class Meta:
        database = database

# Test.create_table() #新建数据表


# p = Test(type=1,name="wangbo")
# p.save(); 新增


# 删
# 单条删除
#
# st = StudentsInfo.get(student_name='hom')
#
# st.delete_instance()
#
# 等同于DELETE
# from student_info where
#
# student_name = 'hom'
#
# 多条删除
#
# StudentsInfo.delete().where(StudentsInfo.student_no < 883).execute()
#
# 等同于DELETE
# from student_info where
#
# student_no < 883



# 查
'''
p = Link.select()
for d in p:
    print(d.name)
'''

# p = Link.get(Link.name == "米醋儿")
# print(p.name)


# 使用where().get()模糊查询
# p = Link.select().where(Link.name % '%醋儿%').get()


# p = Link.select().where(Link.name % '%醋儿%').order_by(Link.id.asc())  排序
# p = Link.select().where(Link.name % '%醋儿%').order_by(Link.id.desc())
# for r in p:
#     print(r.name)



# 改
# 方法1指定数据
#
# StudentsInfo.update(student_no=890).where(StudentsInfo.student_name == 'baby').execute()
#
# 方法2依据原有数据自动更新
#
# StudentsInfo.update(student_no=StudentsInfo.student_no + 1).where(StudentsInfo.student_name == 'baby').execute()
#
# 方法3 多字段更新
#
# StudentsInfo.update(student_no=890,student_name='lady').where(StudentsInfo.student_name == 'baby').execute()
exit()
# 查询多条数据
Links = Link.select().where(Link.is_relative == True)
for p in Links:
    print(p.name, p.birthday, p.is_relative)



# 教程参考https://www.jianshu.com/p/8d1bdd7f4ff5
# http://www.51testing.com/html/38/488838-3715524.html
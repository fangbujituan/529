import sqlite3

# 1、打开数据库的连接
con = sqlite3.connect("test.db")

# 2、打开游标
cur = con.cursor()

# 3、使用游标的execute方法执行任意sql语句
cur.execute('''
    create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    age integer )
''')

# 4、关闭游标
cur.close()

# 5、关闭数据库连接
con.close()
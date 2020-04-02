"""
事务是由一步或者多条数据库操作序列组成的逻辑执行单元
事务的四个特性：ADIC性
    ①原子性（Atomicity）
    ②一致性
    😍隔离性
    ④持续性
    
"""
import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()
# 执行DML语句
c.execute('insert into user_tb values(null, ?, ?, ?)',('aaa', 'bbb'))
c.execute('create table hah (_id integer primary key)')

# 关闭资源
c.close()
conn.close()
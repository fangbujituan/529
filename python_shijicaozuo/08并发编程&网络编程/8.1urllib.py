import urllib.parse

# urlparse（）：用于解析URL字符串，将URL字符串解析成各部分。返回值为ParseReult（tuple的子类）
# urlunparse（）：用于将URL各（ParseReult或者tuple的子类）部分恢复成URL字符串。

s = 'http://www.crazyit.org:80/index.html;abc?name=yeeku#myfree'
# 解析url字符串
r = urllib.parse.urlparse(s)
print(r)    # ParseReult对象元组

tu = ('http', 'www.crazyit.org:80', '/index.html', 'abc', 'yeye', 'yan')
# 恢复查询字符串
uu = urllib.parse.urlunparse(tu)
print(uu)
print('-'*30)


# parse_qs（），parse_qsl（）：用于查询字符串，得到字典或者列表
# urlencode(）：将列表或字典恢复成查询字符串
qs = "'name=faggda&name=ggg&age=18"
print(urllib.parse.parse_qs(qs))
print(urllib.parse.parse_qsl(qs))

t = [("'name", 'faggda'), ('name', 'ggg'), ('age', '18')]
# 将列表恢复成字符串
print(urllib.parse.urlencode(t))

# 小结：
# 1、网络分层及Python对应的网络
# 2、使用urllib.parse解析、恢复URL
# 3、使用urllib.parse解析、恢复查询字符串
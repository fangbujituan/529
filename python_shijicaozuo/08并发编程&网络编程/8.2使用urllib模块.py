"""
目标：
    1、打开URL对应的资源
    2、发送请求参数
    3、发送不同的请求
    4、读取受保护的资源
data：2019.8.15
"""
import urllib.request
import urllib.parse

with urllib.request.urlopen('http://www.crazyit.org/index.php') as f:
    print(f.read().decode('UTF-8'))

# GET请求参数
parse_g = {'name':'yan', 'password':'asdfg'}
with urllib.request.urlopen('http://www.crazyit.org/get.jsp?%s'%urllib.parse.urlencode(parse_g)) as f:
    print(f.read().decode('UTF-8'))

# GET请求参数
parse_p = {'name':'yan', 'password':'asdfg'}
with urllib.request.urlopen('http://www.crazyit.org/post.jsp', date=urllib.parse.urlencode(parse_p).encode('UTF-8')) as f:
    print(f.read().decode('UTF-8'))

# PUT请求参数(PATCH/DELETE)
parse_P = 'put数据'.encode('utf-8')
req = urllib.request.Request(url='http://www.crazyit.org/put', data=parse_P, method='PUT')
with urllib.request.urlopen(req) as f:
    print(f.read().decode('UTF-8'))
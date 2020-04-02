'''
目标：
1、大致理解TCP协议
2、创建socket协议
3、服务端socket操作
'''
# 导包socket
import socket

# 1、创建socket对象:第一个参数，网络；第二个参数，socket类型
s = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM, 0)

# 2、绑定制定ip和端口
s.bind(('192.168.1.1', 8888))

# 3、监听
s.listen()

# 4、接收
while True:
    c, addr = s.accept()    # 接收来自客户端的连接，返回两个参数,与客户端通信的socket和客户端的地址
    c.send('我是服务端，你好'.encode('utf-8'))  # send接收请求
    # 关闭资源
    c.close()
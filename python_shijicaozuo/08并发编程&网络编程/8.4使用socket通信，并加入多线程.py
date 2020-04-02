# 客户端程序
import socket, threading


def read_server(client_socket):
    #  一旦建立连接之后，服务端与客户端虚拟链路建立成功
    while True:
        content = client_socket.recv(2048).decode('UTF-8')
        if content is not None:
            print(content)

client_socket = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM)   # 第一个cs是网络类型，

# 调用connect方法连接服务端
client_socket.connect(('192.168.1.1',8888))
# 将read_server函数以多线程启动，保证能与下死循环并发执行
threading.Thread(target=read_server,args=client_socket)
while True:
    # 获取用户输入
    line = input('')
    if line is None and line == 'exit':
        break
    # 将用户输入写入服务端
    client_socket.send(line.encode('UTF-8'))





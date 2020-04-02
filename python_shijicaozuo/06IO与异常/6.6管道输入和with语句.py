# 管道输入在于：将前一个命令的输出，当成下一个命令的标准输入
# 语法：cmd1 | cmd2 | cmd3
# sys.stdin 代表标准输入


# with语句：
#     使用with语句管理的资源必须是一个实现上下管理协议的类，实现上下管理协议，必须实现两个方法
#
class FkReso:
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        print('该资源的tag：',self.tag)
        return 'fdkasdfk'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('因为异常关闭资源')
        else:
            print('程序正常关闭，关闭资源')

with FkReso('ewfefewf') as fk:
    print("fk为:", fk)
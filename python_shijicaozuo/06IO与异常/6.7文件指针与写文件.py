def seek_op():
    # 文件指针
    with open('6.7文件指针与写文件.py', 'rb', True) as f:
        print(f.tell())

        f.seek(3)

# seek_op()

def rb_read():
    # 二进制模式打开文件
    with open('info.txt', 'w', True) as f:
        # 输出字符串
        f.write("人生苦短，我用python".encode('UTF-8'))
rb_read()
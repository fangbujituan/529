try:
    f = open('aaa.txt', 'rb')
    data = f.read()
    print(data)
except OSError as e:
    # 捕捉所有的异常
    print(e)
finally:
    print("关闭文件")
    f.close()
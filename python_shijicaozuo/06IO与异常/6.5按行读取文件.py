# 按行读取文件
def read_line(file):
    try:
        f = open(file, 'r', True, 'UTF-8')
        # 采用循环一直读取
        while True:
            line = f.readline()
            # 如果没有读取一行，说明文件已经读完
            if not line:
                break
            else:
                print(line)
    except:
        print()
    finally:
        f.close()

# 用for读取
def read_for(file):
    try:
        f = open(file, 'r', True, 'UTF-8')
        for line in f:
            print(line, end=' ')
    except:
        print()
    finally:
        f.close()

# linecache读文件
import linecache
def read_linecache(file):
    try:
        for line in linecache.getlines(file):
            print(line, end='')
    except:
        pass


# read_line('6.5按行读取文件.py')
# read_for('6.5按行读取文件.py')

# read_linecache('6.5按行读取文件.py')
read_linecache(linecache.__file__)


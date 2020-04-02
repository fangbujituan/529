import sys
print("命令如下：")

for i in sys.argv:
    print(i,end='\n')
print('\n\nPython 路径为：', sys.path, '\n')
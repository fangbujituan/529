"""
内容：文件
    打开一个文件用open()方法(open()返回一个文件对象，它是可迭代的)：
     f = open('test.txt', 'r')
     如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
data：2019.6.19
"""
f = open('aaa.txt')

boy = []
girl = []
for each_line in f:
    if each_line[:6] != '====':
        (role, line_spoken) = each_line.s

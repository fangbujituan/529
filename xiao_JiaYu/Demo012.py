'''
* 内容：文件
*   今天来学习一下问价操作
* data ：2019.06.19
* @author：fangbu
'''

# 封装:保存文件
def save_file(boy, girl, count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')
    # 写入boy和girl的内容
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    # 关闭文件
    boy_file.close()
    girl_file.close()
def split_file(file_name):

    # 打开文件
    f= open(file_name)
    # 操作文件
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '====':
            role = each_line.split(':',1)[0]
            line_spoken = each_line.split(':',1)[0]
            if role == 'fangbu':
                boy.append(line_spoken)
            if role == 'xiaochao':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1
    save_file(boy, girl, count)

    # 关闭文件
    f.close()

split_file('D:/pythonio/abc.txt')
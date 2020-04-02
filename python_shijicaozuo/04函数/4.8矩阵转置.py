# 1、使用循环进行矩阵转置
# 2、使用zip函数转置
# 3、使用numpy模块转置
"""
                 1  2  3  4
                 5  6  7  8
                 9 10 11 12
 转置之后（行变列，列变行）：
                 1  5  9
                 2  6 10
                 3  7 11
                 4  8 12

"""
# 矩阵：matrix =  [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
matrix =  [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

# 打印矩阵的方法
def printmatrix(m):
    for ele in m:
        for e in ele:
            print('%2d' % e,end=' ')
        print()

# 方法1，循环转置
def transformatrix(m):
    # m[0]有几个元素，就说明原矩阵就有多少列
    # 列转行
    rt = [[] for i in m[0]]
    for ele in m:
        for i in range(len(ele)):
            rt[i].append(ele[i])
    return rt

# 方法2，zip函数
def transformatrix_zip(m):
    # zip函数转置
    # 你想参数收集，将矩阵中多个列表转换成多个参数，传给zip
    return list(zip(*m))

# 方法3，模块转置
def transformatrix_numpy(m):
    # 使用numpy的内置transpose（）函数
    import numpy
    return numpy.transpose(m).tolist()

printmatrix(matrix)
print('-' * 12)
printmatrix(transformatrix(matrix))
print('-zip' * 12)
printmatrix(transformatrix_zip(matrix))
print('-ku' * 12)
printmatrix(transformatrix_numpy(matrix))
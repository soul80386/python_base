import numpy as np 

"""
===========================================
目录：
1、numpy.zeros 0填充数组
2、numpy.ones  1填充数组
3、numpy.full  指定值填充数组
4、numpy.eye   单位矩阵（对角为1其他为0）
5、numpy.empty 空矩阵（未初始化）
6、numpy.linspace 指定的间隔内返回均匀间隔的数字
7、numpy.arange 在给定间隔内返回均匀间隔的值，返回的是 ndarray
==========================================
1
numpy.zeros(shape, dtype=float, order='C')
返回：返回来一个给定形状和类型的用0填充的数组；
参数：shape:形状
dtype:数据类型，可选参数，默认numpy.float64
order:可选参数，c代表与c语言类似，行优先；F代表列优先
[[1,2],
[3,4]]
如果我们按照C语言的方式存储它，也就是行优先存储的话，那么在内存中，它的形状是这样的：
1,2,3,4
另一派存储方式，也就是列优先存储，它的代表是Fortran语言。上面的数组在内存中的形状就是这样的了：
1,3,2,4
"""
z1 = np.zeros(10, dtype=int)
z2 = np.zeros((3,3))
print("z1:",z1)
#z1: [0 0 0 0 0 0 0 0 0 0]
print("z2:",z2)
#z2: [[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]]

"""
2
numpy.ones(shape, dtype=float, order='C')
返回：返回来一个给定形状和类型的用1填充的数组；
参数同zeros
"""
o1 = np.ones((2,3))
print("o1:",o1)
#o1: [[1. 1. 1.] [1. 1. 1.]]
o2 = np.ones((2,3,4), dtype=int)
print("o2:",o2)
#o2: [[[1 1 1 1]  [1 1 1 1]  [1 1 1 1]]
#     [[1 1 1 1]  [1 1 1 1]  [1 1 1 1]]]

"""
3
numpy.full(shape, fill_value, dtype=float, order='C')
返回：返回来一个给定形状和类型的用fill_value填充的数组；
参数同zeros
"""
f1 = np.full((2,2), 3.14)
print("f1:",f1)
#f1: [[3.14 3.14] [3.14 3.14]]
f2 = np.full((2,2), 3.14, dtype=int)
print("f2:",f2)
#f2: [[3 3] [3 3]]

"""
4
numpy.eye(N, M=None, k=0, dtype=float, order='C')
返回:返回一个对角线元素为1，其他元素为0的二维数组
参数：
N : 整数,返回数组的行数；
M : 整数，可选,返回数组的列数。如果不赋值的话，默认等于N；
k : 整数, 可选,对角线序列号: 0 对应主对角线；,整数对应upper diagonal,负数对应lower diagonal；
"""
e1 = np.eye(3)
print("e1:",e1)
e2 = np.eye(3, 2,dtype=int)
print("e2:",e2)
e3 = np.eye(3, k=3, dtype=int)
print("e3:",e3)
e4 = np.eye(3, k=-1, dtype=int)
print("e4:",e4)
e5 = np.eye(3,4 ,2, dtype=int)
print("e5:",e5)

"""
5
numpy.empty(shape, dtype=float, order='C')
返回：返回来一个给定形状和类型的空数组；
参数同zeros
未初始化的数组，数组的值是内存空间中的任意值 
"""
em1 = np.empty(3)
print("em1:",em1)
em2 = np.empty((2,2), int)
print("em2:",em2)

"""
6
numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None)
返回：返回在指定范围内的均匀间隔的数字（组成的数组），也即返回一个等差数列
参数：
start: 起始点
stop: 结束点, 依据endpoint会有变化, endpoint为True, 则包含显示, 当为False, 不包含(生成序列相当于原始num上加1按endpoint = True生成, 结果只显示第一个到倒数第二个)
num: 元素个数，默认为50, 必须是非负数，
endpoint: 是否包含stop数值，默认为True，包含stop值；若为False，则不包含stop值
retstep: 返回值形式，默认为False，返回等差数列组，若为True，则返回结果(array([`samples`, `step`]))
dtype: 返回结果的数据类型
"""
l1 = np.linspace(0,10,3)
print("l1:",l1)
#l1: [ 0.  5. 10.]
l2 = np.linspace(0,10,3,endpoint=False)
print("l2:",l2)
#l2: [0.         3.33333333 6.66666667]
l3 = np.linspace(0,10,4)
print("l3:",l3)
#l3: [ 0.          3.33333333  6.66666667 10.        ]
l4 = np.linspace(0,10,4,retstep=True)
print("l4:",l4)
#l4: (array([ 0.        ,  3.33333333,  6.66666667, 10.        ]), 3.3333333333333335)

"""
7
numpy.arange(start, stop, step, dtype = None)
返回：在给定间隔内返回均匀间隔的值，返回的是 ndarray
参数：
start: 开始位置，数字，可选项，默认起始值为0
stop: 停止位置，数字，输出结果不包括stop
step: 步长，数字，可选项， 默认步长为1，如果指定了step，则还必须给出start。
dtype: 输出数组的类型。 如果未给出dtype，则从其他输入参数推断数据类型。
注意：对于浮点参数（参数为浮点），结果的长度为ceil（（stop - start）/ step）） 由于浮点溢出，此规则可能导致最后一个元素大于stop
"""
r1 = np.arange(1,5,2)
print("r1:",r1)
#r1: [1 3]
r2 = np.arange(5)
print("r2:",r2)
#r2: [0 1 2 3 4]
r3 = np.arange(1, 2.2, 0.6)
print("r3:",r3)
#r3: [1.  1.6 2.2]
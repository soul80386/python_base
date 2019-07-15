import numpy as np 

"""
目录
"""

"""
1
numpy.random.randint(low, high=None, size=None, dtype='l')
返回: 返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)。
如果没有写参数high的值，则返回[0,low)的值。
参数:
low: 生成的数值最低要大于等于low。
（hign = None时，生成的数值要在[0, low)区间内）
high: 如果使用这个值，则生成的数值在[low, high)区间。
size: 输出随机数的尺寸
dtype: 输出的格式。

"""
for _ in range(4):
    np.random.seed(0)
    r1 = np.random.randint(10)
    print(r1)
x1 = np.random.randint(10)
print(x1)
np.random.seed(0)
x2 = np.random.randint(10)
print(x2)
#始终输出5 5 5 5 0 5

y1 = np.random.randint(10, size=12)
print("y1:", y1)
y2 = np.random.randint(10, size=(3, 4))
print("y2", y2)
y3 = np.random.randint(10, size=(3, 2, 2))
print("y3:", y3)

"""
2
属性                说明
ndarray.ndim        秩，即轴的数量或维度的数量
ndarray.shape       数组的维度，对于矩阵，n 行 m 列
ndarray.size        数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype       ndarray 对象的元素类型
ndarray.itemsize    ndarray 对象中每个元素的大小，以字节为单位
ndarray.flags       ndarray 对象的内存信息
ndarray.real        ndarray元素的实部
ndarray.imag        ndarray 元素的虚部
ndarray.data        包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
"""
print("ndim----y1:",y1.ndim,"--y2:",y2.ndim,"--y3:",y3.ndim)
#ndim----y1: 1 --y2: 2 --y3: 3
print("shape----y1:",y1.shape,"--y2:",y2.shape,"--y3:",y3.shape)
#shape----y1: (12,) --y2: (3, 4) --y3: (3, 2, 2)
print("size----y1:",y1.size,"--y2:",y2.size,"--y3:",y3.size)
#size----y1: 12 --y2: 12 --y3: 12
print("dtype----y1:",y1.dtype,"--y2:",y2.dtype,"--y3:",y3.dtype)
#dtype----y1: int32 --y2: int32 --y3: int32
print("itemsize----y1:",y1.itemsize,"--y2:",y2.itemsize,"--y3:",y3.itemsize)
#itemsize----y1: 4 --y2: 4 --y3: 4
print("flags----y1:",y1.flags,"--y2:",y2.flags,"--y3:",y3.flags)
#内存信息-略
print("real----y1:",y1.real,"--y2:",y2.real,"--y3:",y3.real)
#同数组内容
print("imag----y1:",y1.imag,"--y2:",y2.imag,"--y3:",y3.imag)
#均为0
print("data----y1:",y1.data,"--y2:",y2.data,"--y3:",y3.data)
#data----y1: <memory at 0x000002369C517408> --y2: <memory at 0x000002369C42CA68> --y3: <memory at 0x000002369B289318>

"""
3

"""
#1）使用索引获取数组数据
#索引可以使用负数
print("y1--y1[1]:",y1[1])
#y1--y1[1]: 3
print("y2--y2[1]:",y2[1])
#y2--y2[1]: [7 8 1 5]
print("y3--y3[1]:",y3[1])
#y3--y3[1]: [[0 2] [3 8]]
print("y2--y2[1,1]:",y2[1,1])
#y2--y2[1,1]: 8
print("y2--y2[1][1]:",y2[1][1])
#y2--y2[1][1]: 8
print("y3--y3[1][1][1]:",y3[1][1][1])
#y3--y3[1][1][1]: 8
print("y3--y3[1,1,1]:",y3[1,1,1])
#y3--y3[1,1,1]: 8

#2）使用索引修改数组数据
#和 Python 列表不同，NumPy 数组是固定类型的。
# 这意味着当你试图将一个浮点 值插入一个整型数组时，浮点值会被截短成整型。
# 并且这种截短是自动完成的，不会给你 提示或警告
print("y1:",y1)
#y1: [0 3 3 7 9 3 5 2 4 7 6 8]
y1[1] = 0
print("y1:", y1)
#y1: [0 0 3 7 9 3 5 2 4 7 6 8]
print("y2[1]:",y2[1])
#y2[1]: [7 8 1 5]
y2[1] = 0
print("y2[1]:",y2[1])
#y2[1]: [0 0 0 0]



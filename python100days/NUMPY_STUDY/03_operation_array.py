import numpy as np 

"""
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
r1 =np.random.randint(10)
print(r1)
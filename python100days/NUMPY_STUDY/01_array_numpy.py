import numpy as np 

nparray1 = np.array([1,5,7,3,2])
print(nparray1,type(nparray1))
#[1 5 7 3 2] <class 'numpy.ndarray'>

#不同于 Python 列表，NumPy 要求数组必须包含同一类型的数据。如果类型不匹 配，NumPy 将会向上转换（如果可行）。
nparray2 = np.array([1.6,8,6,0,3])
print(nparray2,type(nparray2))
#[1.6 8.  6.  0.  3. ] <class 'numpy.ndarray'>

#如果希望明确设置数组的数据类型，可以用 dtype 关键字：
nparray3 = np.array([1,2,3,0.9], dtype="int_")
print(nparray3,type(nparray3))
#[1 2 3 0] <class 'numpy.ndarray'>

#不同于 Python 列表，NumPy 数组可以被指定为多维的。
nparray4 = np.array([range(i, i+3) for i in [2, 3, 4]])
print(nparray4)
#[[2 3 4] [3 4 5] [4 5 6]]

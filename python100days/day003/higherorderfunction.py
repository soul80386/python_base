"""
高阶函数：
把函数作为参数传入，这样的函数称为高阶函数
"""

#变量可以指向函数
a = max(1,2,3)
print(a,type(a)) #此时a是一个整数
a = max
print(a,type(a),a(1,2,3,4)) #此时a是一个指向max()的函数

#函数名其实就是指向函数的变量
a = [1,2,3]
print(max(a)) # 3
max = [3,4,5]
#print(max(1,2,3)) #报错，TypeError 此时max指向的是列表[3,4,5],不再指向max()函数
#代码不能这么写，要恢复max()函数，需重启python交互环境

"""
将函数作为参数
"""
def add(x,y,f):
    return f(x) + f(y)
print(add(-4,5,abs))

def test(x, y):
    return x ** y
print(test(3,3))

def test1(x,y,f):
    return f(x,y) + f(y,x)
print(test1(2,3,test)) # 2^3 + 3^2 = 17
"""
列表生成式
"""
L1 = [x // 10 for x in range(100) if x % 5 ==0]
print(L1)

S1 = {x * x for x in range(10) if x % 3 == 1}
print(S1)

L2 = [m + n for m in 'ABC' for n in 'abc']
print(L2)

"""
生成器：一边循环一边计算的机制，称为生成器:generate
生成器保存的是算法
将列表生成式的[]改为()，即可创建生成器
"""
#创建生成器方法一
G1 = (x**3 for x in range(10) if x % 2 == 1)
print(next(G1))
for i in G1:
    print(i)

#创建生成器方法二：yield
#斐波那契数列：使用生成器
"""
以下定义的fib不是普通函数，而是一个生成器generate
在执行过程中，遇到yield就中断，下次继续执行
"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

"""
杨辉三角使用生成器实现
"""

for i in fib(10):
    print(i)

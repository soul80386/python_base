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
def fib():
    n, a, b = 0, 0, 1
    while True:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

n = 0
for i in fib():
    print(i)
    n += 1
    if n ==10:
        break

"""
杨辉三角使用生成器实现
"""
def triangles():
    p = [1]
    while True:
        yield p
        #新的一行，首尾为1，中间部分为逐个依次相加（第一个元素为p[0],最后一个元素是p[len(p)-1]
        p = [1] + [p[i] + p[i + 1] for i in range(len(p)-1)] + [1]

t = 0
for i in triangles():
    print(i)
    t += 1
    if t == 11:
        break

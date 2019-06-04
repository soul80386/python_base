#导入模块简例：crapsgame.py在同一目录下
#import crapsgame as c
#print(c.crapsrandom())

"""
练习
"""
#练习1：实现求最大公约数和最小公倍数

def gcd(x,y):
    for i in range(min(x,y),0,-1):
        if x % i == 0 and y % i == 0:
            return i

def lcm(x,y):
    return x * y //gcd(x, y)

##print(lcm(2,3))

#练习2：判断一个数是不是回文数，回文数：如12321，4554
def is_palindrome(num):
    tmp = num
    totle = 0
    while tmp > 0:
        #将输入数从右向左逐位取出并从左至右排列
        totle = totle * 10 + tmp % 10
        tmp //= 10
    return totle == num

#print(is_palindrome(12331))

#练习3：判断一个数是不是素数：除了1和它自身没有其他自然数因子
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True if num != 1 else False

#print(is_prime(5))


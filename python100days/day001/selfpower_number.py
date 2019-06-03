"""
寻找水仙花数：
水仙花数指一个3位数，它的每个位上的数字的3次幂之和等于它本身
例如：1^3+5^3+3^3 = 153
"""
def test():
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                if i**3 + j**3 + k**3 == i*100 + j*10 + k:
                    print(i*100 + j*10 + k)

def selfpowerNumber(num):
    if num < 1:
        print('请输入大于等于1的整数！')
    elif num > 9:
        print('位数较高计算量较大，请输入小于等于9的数值')
    else:
        #根据输入位数值确定循环数据范围：如3位数（10^2,10^3-1)(100-999)
        for i in range(10**(num-1),10**num):
            #初始化每个位上数字自幂求和
            num_sum = 0
            #每个位上数字自幂求合
            for j in range(num):
                #从个位数起逐位取值求自幂值
                #依位地板除后求模取得每位数字
                num_sum += ((i // (10**j)) % 10) ** num
            if num_sum == i:
                print(i)
#未做输入异常处理
num = int(input('请输入寻找自幂数的位数：'))
selfpowerNumber(num)




            

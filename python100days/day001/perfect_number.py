"""
寻找完全数：
完全数指：它所有的真因子（除自身以外的约数）之和，恰好等于它自身
如6，真因子有：1，2，3，1+2+3=6
"""

def perfect_number(num):
    for i in range(1,num):
        num_sum = 0
        for j in range(1,i//2 +1):            
            if i % j == 0:
                num_sum += j
        if i == num_sum:
            print(i)

perfect_number(100000)

"""
craps赌博游戏：
玩家掷两个骰子，点数为1-6，
如果第一次点数和为7或11，玩家胜
    第一次点数和为2、3、12，玩家输
如果为其他点数，记录第一次点数和，然后继续掷骰子
    直至点数和等于第一次掷骰点数和，玩家胜
    如果过胜之前掷出和为7，玩家输
"""
import random
import math
def crapsrandom():
    x = math.floor(random.random() *10) + 1
    while x > 6:
        x = math.floor(random.random() *10) + 1
    return x
def carpsgame():
    a = crapsrandom()
    b = crapsrandom()
    first_sum = a + b
    if first_sum == 7 or first_sum == 11:
        print('你赢了！你掷出了%d和%d，合%d'%(a,b,first_sum))
    elif first_sum == 2 or first_sum == 3 or first_sum == 12:
        print('你输了><!你掷出了%d和%d，合%d'%(a,b,first_sum))
    else:
        print('未分胜负!你掷出了%d和%d，合%d'%(a,b,first_sum))
        count = 2
        while count > 1:
            x = crapsrandom()
            y = crapsrandom()
            if x + y == 7:
                print('你第%d次掷出了%d,%d，你输了！你第一次掷出的点数为：%d,%d,合%d'%(count,x,y,a,b,first_sum))
                break
            elif x + y ==first_sum:
                print('你第%d次掷出了%d,%d，你赢了！你第一次掷出的点数为：%d,%d,合%d'%(count,x,y,a,b,first_sum))
                break
            else:
                print('你第%d次掷出了%d,%d，未分胜负！你第一次掷出的点数为：%d,%d,合%d'%(count,x,y,a,b,first_sum))
                count +=1
                continue

carpsgame()


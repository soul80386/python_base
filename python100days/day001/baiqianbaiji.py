def bqbj1():
    for i in range(21):
        for j in range(33):            
            if 5 * i + 3 * j + (100- i - j) / 3 == 100:
                print('公鸡：%d,母鸡：%d,小鸡：%d'%(i,j,(100-i-j)))
if __name__ == '__main__':
    bqbj1()
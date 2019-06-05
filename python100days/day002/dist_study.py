"""
dist：字典，部分语言中称为map
使用key-value（键-值）的方式存储
特点：具有极快的查找速度，占用较大的内存
要求：key必须是不可变对像
"""
def main():
    #声明dist
    dist1 = {'a':None,'b':None,'c':None}
    print(type(dist1)) #<class 'dist'>
    dist1.update(d=1)
    print(dist1)

if __name__ == "__main__":
    main()
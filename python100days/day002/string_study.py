def main():
    str1 = 'Helloworld'
    print(str1)
    #首字母转大写
    print(str1.capitalize())
    #字符串转大写
    print(str1.upper())
    #字符串转小写
    print(str1.lower())
    #查找字符串,没有返回-1
    print(str1.find('or'))
    print(str1.find('and'))
    #指定长度，在两端填充指定字符
    print(str1.center(20,'*'))
    print('ab'.center(5,'*'))
    print('abc'.center(6,'*'))
    #指定长度，在左/右侧填充指定字符
    print(str1.ljust(20,'-'))
    print(str1.rjust(20,'-'))
    #下标运算，取指定位置字符
    print(str1[1])
    #字符切片
    print(str1[5:-2]) #负数为倒数位置
    print(str1[:1])
    print(str1[:6])
    print(str1[-1:-3]) #结束位置小于1，无输出
    str2 = '123456'
    #取前5个字符，每隔两个字符取一个
    print(str2[:5:2])  #1，3，5
    print(str2[::3])
    #从倒数第一个字符开始，每隔-1个取一个字符，倒序
    print(str2[::-1]) #654321
    #判断字符串是否是数字构成
    print(str1.isdigit())
    print(str2.isdigit())
    #判断字符串是否是字母构成
    print(str1.isalpha()) #只能包含字母



if __name__ == "__main__":
    main()    
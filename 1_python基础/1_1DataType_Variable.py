# 变量命名
'''
-变量命名规则：
    -变量名必须是大小写英文、数字和_的组合
        -不建议使用_、__（单下划线和双下划线开头，有特殊含义）
    -不能用数字开头
        -5man，这样的变量名是不允许的
    -python对大小写敏感，man与Man不是同一个变量
    -通常全部大写表示常量
-驼峰命名法
    -大驼峰：通常用于类命名
        -CatOne 每个单词第一个字母大写
    -小驼峰：通常用于变量或函数命名
        -firstDog 类似大驼峰，第一个字母小写 
    -posix写法：int_one
-保留字和关键字
    -关键字如：class, def, for
    -保留字: 语言系统自留字符串
'''

# 查看关键字和保留字
import keyword
print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'if',  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
 'try', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#声明变量
'''
-声明方式
    -1：var_name = var_value
    -2：var1 = var2 = var3 = var_value
        -python解释器做了两件事
            -1）在内存中创建了var_value的值
            -2）在内存中创建了var1, var2, var3 三个变量
        -后续代码中改变var1, var2, var3中任一变量的值，不影响另外两个变量    
    -3：var1, var2, var3 = v1, v2, v3
-其他说明
    -这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
        -如JAVA声明：int a = 123;
        -变量a是整型变量，将字符串赋值给a将报错：a = "ABC"是错误的
    -=号是赋值，判断相等是==
'''

# 变量类型
'''
-严格意义上来说，python只有一个类型，可以把任何数据类型都看成是一个对象，
 变量就是在程序中指向这些数据对象的

-整数
    -python可以处理任意大小的整数，即没有大小限制
    -自然数、0、负自然数
    -整数分进制
        -二进制
            -计算机常用，是计算机唯一能理解的数字
            -表示为0b开头的0、1代码
            -如：0b10101，相当于十进制21
        -八进制
        -十进制
        -十六进制

'''
print(0b10101)
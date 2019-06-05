"""
set集合与数学上的集合是一致的
set是无序的
不允许有重复元素
可以进行交集、并集、差集等运算
"""

def main():
    #声明set，可以使用{}，或者set()函数创建集合
    set1 = {1,2,3,4,5}
    #使用set()函数创建set，需传入一个列表作为参数
    set2 = set(['a','b','c','d','e'])
    print(type(set1),type(set2))

    #set的元素不允许有重复值，声明重复的值将被忽略
    set3 = {1,1,2,2,3,3,3}
    print(set3,len(set3)) #输出 {1,2,3} 3

    """
    set操作
    """
    #添加元素
    set1.add(5)
    print(set1)
    #添加已有的元素，不会有效果
    set1.add(1)
    print(set1)
    #删除元素,删除指定元素值的元素
    set1.remove(1)
    print(set1)
    #删除不存在的元素，报错 KeyError
    #set1.remove(6)
    #正确姿势
    if 6 in set1:
        set1.remove(6)

    #set的交集、并集、差集、对称差运算
    set01 = {1,2,3,4,5}
    set02 = {3,4,5,6,7}
    set03 = {4,5,6}
    print(set01,set02,'交集',set01 & set02) #{3，4，5}
    print(set01,set02,'并集',set01 | set02) #{1,2,3,4,5,6,7}
    print(set01,set02,'差集',set01 - set02) #{1，2}
    print(set01,set02,'差集',set02 - set01) #{6，7}
    print(set01,set02,'对称差',set01 ^ set02) #{1，2，6，7}
    #判断子集和超集
    print(set02 >= set03) #True
    print(set02.issubset(set03)) #False set02是否是set03的子集
    print(set02.issuperset(set03)) #True set02是否是set03的超集

if __name__ == "__main__":
    main()
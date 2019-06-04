"""
list是一种有序的集合
list是一个可变的有序表
list中的元素的数据类型可以不相同
"""
def main():
    #list声明
    list1 = ['one','two','three']
    print(list1)
    #获取列表长度
    print(len(list1)) #3

    #list索引,索引从0开始,可以使用负数完成倒数索引
    #索引值不能大于长度-1
    print(list1[1])
    print(list1[-1])
    #print(list1[3]) #索引超界,错误 IndexError

    """
    在列表中添加元素
    """
    #在末尾添加元素
    list1.append('four')
    print(list1)
    #在指定位置添加元素
    list1.insert(0,'zero')
    print(list1)
    list1.insert(-1,'test')
    print(list1)

    """
    在列表中删除元素
    """
    #删除末尾元素
    list1.pop()
    print(list1)
    #删除指定位置元素
    list1.pop(-1)
    print(list1)
    #删除指定内容的元素,有两个相同元素时，仅删除第一个
    list1.append('one')
    print(list1)
    #list1.remove('other') #删除不存在的元素时，错误 ValueError
    print(list1)

    """
    修改列表元素
    """
    #修改列表元素，重新给指定位置的元素重新赋值即可
    list1[0] = 'other'
    print(list1)
    #列表中的元素可以是列表
    list1[0] = [1,2,3]
    print(list1)
    #此时list1可以看作是一个二维列表
    print(list1[0])
    print(list1[0][1])
    
    #空列表
    L = []
    print(len(L))


if __name__ == '__main__':
    main()
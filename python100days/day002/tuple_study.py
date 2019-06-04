"""
tuple是一种有序列表，叫元组，tuple和list类似
区别在于：tuple一旦初始化就不能修改
"""

def main():
    #tuple声明
    tuple1 = ('one','two','three')
    print(tuple1)
    #声明只有一个元素的tuple，元素后须添加逗号
    tuple2 = (1)
    tuple3 = (2,)
    print(tuple2,type(tuple2),tuple3,type(tuple3))

if __name__ == '__main__':
    main()
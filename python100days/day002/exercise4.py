"""
《幸运的基督徒》
有15个基督徒和15个非基督徒
30个人围成一圈，由某个人开始从1报数，报到9的人就扔到海里，后面的人接着从1开始报数
直到扔掉15个人，15个基督徒都未被扔掉
问：这些人开始是怎么站的
"""

def main():
    persons = [True] * 30
    index, counter, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非',end=' ')

if __name__ == "__main__":
    main()
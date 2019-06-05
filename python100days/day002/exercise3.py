"""
打印杨辉三角
"""
def yhsj():
    while True:
        row_num = input('请输入打印杨辉三角的行数：')
        if row_num.isdigit():
            row_num = int(row_num)
            break
        else:
            print('请输入数字')
    
    yh = [[]] * row_num
    for row in range(row_num):
        yh[row] = [None] * (row + 1)
        for col in range(row+1):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col-1] + yh[row-1][col]
            print(yh[row][col],end='\t')
        print()

if __name__ == "__main__":
    yhsj()
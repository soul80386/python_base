"""
生成指定位数的验证码
验证码由数字和大小写字母组成
"""

import random

def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ''
    #_表示临时名称，且在后续代码中并不会使用到它
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

if __name__ == "__main__":
    print(generate_code(6))
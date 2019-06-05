"""
在屏幕上显示跑马灯文字
"""
import os
import time

def main():
    content = 'good good study! day day up!…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.4)
        content = content[1:] + content[0]

if __name__ == "__main__":
    main()
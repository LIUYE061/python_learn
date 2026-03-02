"""
猜数字
"""

import random
num = random.randint(1,100)
i = 1
flag = 1
while flag:
    num1 = int(input("请输入你猜的数字: "))
    if num1 == num:
        print(f"猜对了,共猜了{i}次")
        flag = 1
    elif num1 > num:
        print("猜大了")
    else:
        print("猜小了")
    i += 1

# 可以用while True: 后续用break跳出
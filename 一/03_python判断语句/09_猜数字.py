"""
完成安利 猜数字

需求: 定义一个数字(1-10, 随机产生), 通过3次判断来猜出数字.

要求:
    1. 数字随机产生, 范围1-10.
    2. 有3次机会, 通过3层判断嵌套实现.
    3. 每次猜不中, 会提示大了小了.

生成随机数:
import random
num = random.randint(1, 10)
"""

import random
num = random.randint(1, 10)
num1 = int(input("请输入你猜的数字(1-10): "))
if num1 == num:
    print("恭喜你, 一次猜对.")
else:
    if num1 > num:
        print("猜大了.")
    else:
        print("猜小了.")
    num2 = int(input("请再次输入你猜的数字(1-10): "))
    if num2 == num:
        print("第二次猜对了.")
    else:
        if num2 > num:
            print("猜大了.")
        else:
            print("猜小了")
        num3 = int(input("最后一次机会, 请输入你猜的数字(1-10): "))
        if num3 == num:
            print("最后一次猜对了.")
        elif num3 > num:
            print("还是大了.")
        else:
            print("还是小了.")


# 可以将num1, num2, num3合为一个变量guess_num
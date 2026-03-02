"""
案例
"""

num1 = 10
if int(input("请输入第一次猜想的数字: ")) == num1:
    print("猜对了.")
elif int(input("不对, 再猜一次: ")) == num1:
    print("猜对了.")
elif int(input("不对, 再猜最后一次: ")) == num1:
    print("猜对了.")
else:
    print(f"全部猜错了, 我想的是: {num1}")
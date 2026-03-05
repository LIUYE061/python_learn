"""
演示python的闭包特性
"""
from numpy.ma.core import inner


# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# fn1 = outer("heima")
# fn1("hello")
#
# fn2 = outer("chuanzhi")
# fn2("hello")

# 使用nonlocal关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
# fn = outer(10)
# fn(15)
# fn(15)

# 使用闭包实现ATM小案例
def account_create(initial_amount = 0):

    def atm(num, deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
        else:
            initial_amount -= num
        return initial_amount

    return atm

atm = account_create()
print(atm(100))
print(atm(200))
print(atm(100, False))
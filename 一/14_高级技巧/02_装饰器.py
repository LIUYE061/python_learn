"""
演示装饰器的写法
"""
from numpy.ma.core import inner
import time
import functools


# 装饰器的一般写法(闭包)
# def outer(func):
#
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 5))
#
# # print("我睡觉了")
# # sleep()
# # print("我起床了")
#
# sle = outer(sleep)
# sle()

# 装饰器的快捷写法(语法糖)
# def outer(func):
#
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
# @outer
# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 5))
#
# sleep()

# @property 装饰器
# class Circle:
#     def __init__(self, radius = None):
#         self.__radius = radius
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, new_radius):
#         self.__radius = new_radius
#
#     @radius.deleter
#     def radius(self):
#         del self.__radius
#
# c = Circle()
# print(c.radius)
# c.radius = 10
# print(c.radius)
# del c.radius

# 计时装饰器
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(result)
#         print("%.1f" %(end_time - start_time))
#         print(end_time - start_time)
#
#     return wrapper
#
# @timer
# def add(x, y) -> int:
#     return x + y
#
# add(1, 2)

# 两个装饰器叠加使用
def f0(func):
    print(3)
    def wrapper(*args, **kwargs):
        print("第一个装饰器star")
        func(*args, **kwargs)
        print("第一个装饰器end")

    print(4)
    return wrapper


def f1(func):
    print(1)
    def wrapper(*args, **kwargs):
        print("第二个装饰器star")
        func(*args, **kwargs)
        print("第二个装饰器end")

    print(2)
    return wrapper

@f0
@f1
def f2(num):
    print(num)

f2(6)
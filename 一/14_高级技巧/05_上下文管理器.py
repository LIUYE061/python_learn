"""
实现上下文管理器
"""

# 用类实现上下文管理器
# class MyOpen:
#     def __init__(self, filepath):
#         print("init")
#         self.filepath = filepath
#
#     def __enter__(self):
#         print("enter")
#         return self.filepath
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit")
#
# with MyOpen("test,txt") as f:
#     print(f)

# 通过生成器函数实现上下文管理器
from contextlib import contextmanager

@contextmanager
def my_open(filepath):
    print("entering my_open")
    try:                              # 相当于__enter__
        yield filepath
    finally:                          #相当于__exit__
        print("exit my_open")

with my_open("test.txt") as f:
    print(f)
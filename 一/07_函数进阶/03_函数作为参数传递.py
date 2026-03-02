"""
演示函数作为参数传递
"""

#  定义一个函数, 接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2)
    print(result, type(compute))

# 定义一个函数, 准备作为参数传入另一个函数
def add(x, y):
    return x + y

# 调用, 并传入函数
test_func(add)
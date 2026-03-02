"""
演示函数的多返回值实例
"""

# 演示使用多个变量, 接收多个返回值
def test_return():
    return 1, "aaa"  # 可以返回不同类型的数据

x, y = test_return()
print(x)
print(y)
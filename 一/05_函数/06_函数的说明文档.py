"""
演示对函数进行文档说明
"""

# 定义函数, 进行文档说明
def add(x, y):
    """
    add 函数可以接受两个参数进行两数相加的函数
    :param x: 形参x 表示相加的其中一个数字
    :param y: 形参y 表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """
    result = x + y
    print(f"结果为: {result}")
    return result

add(5, 6)
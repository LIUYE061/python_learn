"""
演示函数的嵌套调用
"""

# 定义函数func_b
def func_b():
    """
    输出"---2---"
    :return:
    """
    print("---2---")

# 定义函数func_a
def func_a():
    """
    输出123
    :return:
    """
    print("---1---")

    # 嵌套调用func_b
    func_b()

    print("---3---")

# 调用函数func_a
func_a()
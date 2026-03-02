"""
演示多种传参的形式
"""

def user_info(name, age, gender):
    print(f"您的名字是{name}, 您的年龄是{age}, 您的性别是{gender}")

# 位置参数 - 默认使用形式
user_info("TOM", 20, "男")

# 关键字参数
user_info(age = 20, gender = "男", name = "TOM")
user_info("小明", gender = "男", age = 20)

# 缺省参数(默认值)
def user_info(name, age, gender = "男"):
    print(f"您的名字是{name}, 您的年龄是{age}, 您的性别是{gender}")

user_info("TOM", 20)
user_info("ROSE", 20, "女")

# 不定长 - 位置不定长, *号
def user_info(*args):
    print(args, type(args))

user_info("TOM")  # ("TOM", )
user_info("TOM", 18)  # ("TOM", 18)

# 不定长 - 关键字不定长, **号
def user_info(**kwargs):
    print(kwargs, type(kwargs))

user_info(name = "TOM", age = 18, id = 110)  # {"name": "TOM", "age": 18, "id": 110}
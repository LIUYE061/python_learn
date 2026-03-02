"""
练习案例: 分割字符串
"""

# 定义字符串
my_str = "itheima itcast boxuegu"

# 统计有多少个it
print(my_str.count("it"))

# 将空格全部替换为|
new = my_str.replace(" ", "|")
print(new)

# 按照|进行字符串分割, 得到列表
list1 = new.split("|")
print(list1)
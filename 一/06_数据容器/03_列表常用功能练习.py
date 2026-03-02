"""
常用功能练习
"""

# 定义一批学生的年龄
age = [21, 25, 21, 23, 22, 20]

# 追加一个数字31到尾部
age.append(31)
print(age)

# 追加一个新列表[29, 33, 30]到尾部
add = [29, 33, 30]
age.extend(add)
print(age)

# 取出第一个元素21
get = age.pop(0)
print(get)

# 取出最后一个元素30
get = age.pop(-1)
print(get)

# 查找元素31的下标
index = age.index(31)
print(age)
print(index)
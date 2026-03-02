"""
演示数据容器集合的使用
"""

# 定义集合
my_set = {"itcast", "itheima", "python", "itcast", "itheima", "python", "itcast", "itheima", "python"}
my_set_empty = set()
print(f"my_set的内容: {my_set}, 类型是: {type(my_set)}")
print(f"my_set_empty的内容: {my_set_empty}, 类型是: {type(my_set_empty)}")

# 添加新元素
my_set.add("黑马")
print(my_set)

# 移除元素
my_set.remove("itheima")
print(my_set)

# 随机取出一个元素
my_set = {"itcast", "itheima", "python", "itcast", "itheima", "python", "itcast", "itheima", "python"}
element = my_set.pop()
print(element)
print(my_set)

# 清空集合
my_set.clear()
print(my_set)

# 取2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3)

# 消除2个集合的差集
set1.difference_update(set2)
print(set1)
print(set2)

# 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set3)

# 统计集合元素数量
set1 = {1, 2, 3}
print(len(set1))
set2 = {1, 5, 6, 1, 5, 6}
print(len(set2))

# 集合的遍历
for i in set1:
    print(i)
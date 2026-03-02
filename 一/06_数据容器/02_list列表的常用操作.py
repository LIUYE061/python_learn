"""
演示数据容器之: list列表的常用操作
"""

mylist = ["itcast", "itheima", "python"]

# 1.1 查找某元素在列表内的下标索引
index = mylist.index("itheima")
print(f"itheima在列表中的索引值是: {index}")

# 1.2 如果被查找的元素不存在, 会报错
# index = mylist.index("hello")
# print(f"hello在列表中的索引值是: {index}")

# 2 修改特定下标索引的值
mylist[0] = "传智教育"
print(f"元素被修改元素值后的结果是: {mylist[0]}")

# 3 在指定下标位置插入新元素
mylist.insert(1, "best")
print(f"列表插入元素后的结果是: {mylist}")

# 4 在列表的尾部追加 单个 新元素
mylist.append("黑马程序员")
print(f"列表追加元素后的结果: {mylist}")

# 5 在列表的尾部追加 一批 新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加一个新列表后为: {mylist}")

# 6 删除指定下标索引的元素 (两种方式)
mylist = ["itcast", "itheima", "python"]

# 6.1 方式一: del 列表[下标]
del mylist[2]
print(f"删除后: {mylist}")

# 6.2 方式二: 列表.pop(下标)
mylist = ["itcast", "itheima", "python"]
element = mylist.pop(1)
print(f"删除后: {mylist}, 被删元素为: {element}")

# 7 删除某元素在列表中的第一个匹配项
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
mylist.remove("itheima")
print(f"通过remove方法移除元素后列表的结果: {mylist}")

# 8 清空列表
mylist.clear()
print(f"列表被清空了, 内容是: {mylist}")

# 9 统计列表内某元素的数量
mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
count = mylist.count("itheima")
print(f"统计itheima的数量: {count}")

# 10 统计列表中全部的元素数量
count = len(mylist)
print(f"列表的元素数量共有{count}个")
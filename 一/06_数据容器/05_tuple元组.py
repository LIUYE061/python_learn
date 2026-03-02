"""
演示tuple元组的定义和操作
"""

# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)}, 内容是: {t1}")
print(f"t1的类型是{type(t2)}, 内容是: {t2}")
print(f"t1的类型是{type(t3)}, 内容是: {t3}")

# 定义单个元素的元组
t4 = ("hello", )
print(f"t1的类型是{type(t4)}, 内容是: {t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t1的类型是{type(t5)}, 内容是: {t5}")

# 下标索引去取出内容
print(t5[1][2])

# index查找
t6 = ("itcast", "itheima", "python")
index = t6.index("itheima")
print(f"itheima的下标: {index}")

# count统计某个元素的个数
t7 = ("itcast", "itheima", "itcast", "itheima", "python")
num = t7.count("itheima")
print(f"itheima的个数: {num}")

# len统计元组中元素数量
count = len(t7)
print(f"t7中的元素总数: {count}")

# 元组遍历 while
index = 0
while index < len(t7):
    print(t7[index])
    index += 1

# 元组遍历 for
for element in t7:
    print(element)

# 修改元组内容, 报错
# t7[0] = 1

# 但可以修改元组中嵌套的list列表内容
t8 = ((1, 2), ["itcast", "itheima"])
print(f"t8的内容: {t8}")
t8[1][0] = 1
print(f"修改后t8的内容: {t8}")
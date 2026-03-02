"""
集合练习: 信息去重
"""

my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]
# 定义一个空集合
set1 = set()

# for循环遍历列表
for element in my_list:
# 在for循环中将列表的元素添加至集合
    set1.add(element)

# 打印元素去重后的集合对象
print(f"有列表: {my_list}")
print(f"存入集合后结果: {set1}")
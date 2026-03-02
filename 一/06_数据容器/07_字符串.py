"""
演示以数据容器的角色, 学习字符串的相关操作
"""

my_str = "itheima and itcast"
# 通过下标索引取值
print(f"取h:{my_str[2]}")

# index方法
print(f"e的下标: {my_str.index("e")}")
print(f"and的下标: {my_str.index("and")}")

# replace方法
new_my_str = my_str.replace("it", "程序")
print(new_my_str)

# split方法
list1 = my_str.split(" ")
print(list1, type(list1))
list2 = my_str.split("t")
print(list2)

# strip方法
my_str1 = " itheima and itcast "
print(my_str1.strip())
print(my_str1.strip("i t"))

# 统计字符串中某字符串的出现次数
num = my_str.count("i")
print(f"i的个数: {num}")

# 统计字符串的长度
count = len(my_str)
print(f"字符串长度: {count}")
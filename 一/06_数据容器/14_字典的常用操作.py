"""
演示字典的常用操作
"""

my_dict = {"张三": 99, "李四": 88, "王五": 77}

# 新增元素
my_dict["111"] = 66
print(my_dict)

# 更新元素
my_dict["张三"] = 33
print(my_dict)

# 删除元素
score = my_dict.pop("张三")
print(score, my_dict)

# 清空元素
my_dict.clear()
print(my_dict)

# 获取全部的key
my_dict = {"张三": 99, "李四": 88, "王五": 77}
print(my_dict.keys(), type(my_dict.keys()))

# 遍历字典
# 1. 通过获取全部的key
for key in my_dict.keys():
    print(key, my_dict[key])

# 2. 直接对字典进行for循环, 每一次循环都是直接得到key
for key in my_dict:
    print(key, my_dict[key])

# 统计字典内的元素数量
print(len(my_dict))
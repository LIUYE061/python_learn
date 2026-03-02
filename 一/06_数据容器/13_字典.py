"""
演示数据容器字典的定义
"""

# 定义字典
my_dict = {"张三": 99,"李四": 88,"王五": 77}

# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是: {my_dict}, 类型是: {type(my_dict)}")
print(f"字典2的内容是: {my_dict2}, 类型是: {type(my_dict2)}")
print(f"字典3的内容是: {my_dict3}, 类型是: {type(my_dict3)}")

# 定义重复key的字典
my_dict = {"张三": 99,"张三": 88,"王五": 77}
print(f"重复key的字典的内容: {my_dict}")

# 从字典中基于key获取value
my_dict = {"张三": 99,"李四": 88,"王五": 77}
print(my_dict["张三"])
print(my_dict["李四"])

# 定义嵌套字典
my_dict = {"张三": {"语文": 77, "数学": 66, "英语": 33}, "李四": {"语文": 88, "数学": 86, "英语": 55},
           "王五": {"语文": 99, "数学": 96, "英语": 66}}

# 从嵌套字典中获取数据
print(my_dict["张三"]["数学"])
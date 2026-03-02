"""
演示数据容器的通用功能
"""

my_list = [1, 3, 5, 2, 4]
my_tuple = (1, 3, 5, 2, 4)
my_str = "agcebfd"
my_set = {1, 3, 5, 2, 4}
my_dict = {"key3": 3, "key2": 2, "key4": 4, "key1": 1, "key5": 5}

# len 元素个数
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))

# max 最大元素
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

# min 最小元素
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

# 类型转换: 容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))

# 类型转换: 容器转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))

# 类型转换: 容器转字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_set))
print(str(my_dict))

# 类型转换: 容器转集合
print(set(my_list))
print(set(my_tuple))
print(set(my_str))
print(set(my_dict))

# 进行容器的排序
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
print(sorted(my_dict, reverse=True))
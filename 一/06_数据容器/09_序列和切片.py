"""
演示对序列进行切片操作
"""

# 对list进行切片操作, 从1开始, 4结束, 步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
new_my_list = my_list[1: 4]
print(new_my_list)

# 对tuple切片, 从头开始, 到最后结束, 步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[:])

# 对str切片, 从头开始, 到最后结束, 步长2
my_str = "01234567"
print(my_str[::2])

# 对str切片, 从头开始, 到最后结束, 步长-1
my_str = "01234567"
print(my_str[::-1])

# 对list切片, 从3开始, 到1结束, 步长-1
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[3:1:-1])

# 对tuple切片, 从头开始, 到尾结束, 步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[::-2])
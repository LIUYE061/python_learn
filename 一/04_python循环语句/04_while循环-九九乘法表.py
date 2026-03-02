"""
九九乘法表
"""

# print语句输出不换行
# print("hello", end = '')
# print("world", end = '')

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}\t", end = '')
        j += 1
    print()
    i += 1
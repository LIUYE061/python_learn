# 语法1 range(num)
# for i in range(10):
#     print(i)

# 语法2 range(num1, num2)
# for i in range(5, 10):
#     print(i)

# 语法3 range(num1, num2, step)
# for i in range(5, 10, 2):
#     print(i)



# 有几个偶数
num = 100
i = 0
for x in range(1, num):
    if x % 2 == 0:
        i += 1
print(f"1到{num}(不含{num}本身)的范围内, 偶数的个数是{i}")
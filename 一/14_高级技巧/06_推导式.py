# nums = [1, 3, 5, 7, 9]
# nums = (1, 3, 5, 7, 9)

# 正常for循环
# new_nums = []
#
# for num in nums:
#     result = num * 2
#     new_nums.append(result)

# 列表推导式
# new_nums = [num * 2 for num in nums]

# 加入if
# new_nums = [num * 2 for num in nums if num > 3]

# 加入if else
# new_nums = [num * 2 if num > 3 else num for num in nums]

# print(new_nums)

# 字典推导式
# li = ["name", "age", "gender"]
#
# dic = {key: key.upper() for key in li}
#
# print(dic)

# 集合推导式
# import random
#
# s1 = {random.randint(1, 100) for i in range(10)}
#
# print(s1)

# 生成器表达式
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0 :
                return False
        return True

for prime in (i for i in range(101) if is_prime(i)):
    print(prime)
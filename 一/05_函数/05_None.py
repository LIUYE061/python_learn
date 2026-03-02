# 无return语句的函数返回值
def say_hi():
    print("hi")

i = say_hi()
print(type(i))

# 主动返回None的函数
def say_hi2():
    print("hi2")
    return None

print(type(say_hi2()))

# None用于if判断
def check_age(age):
    if age > 18:
        return "Success"
    else:
        return None

result = check_age(16)
if not result:
    print("未成年")

# None用于声明无初始内容的变量
name = None
"""
演示python的input语句
获取键盘的输入信息
"""
# print("请告诉我你是谁? ")
name = input("请告诉我你是谁?")
print("我知道了, 你是: %s" % name)

# 输入数字类型
num = input("请告诉我你的银行卡密码: ")
# 数字类型转换
num = int(num)
print("你的银行卡密码是的类型是: " , type(num))

# 欢迎登陆小程序
user_name = input("请输入用户名称: ")
user_type = input("请输入用户类型: ")
print(f"您好: {user_name}, 您是尊贵的: {user_type}用户, 欢迎您的光临.")
"""
演示 if elif else语句的使用
"""

if int(input("请输入你的身高(cm): ")) < 120:
    print("身高小于120cm, 可以免费游玩.")
elif int(input("请输入你的VIP等级(1-5): ")) > 3:
    print("VIP级别大于3, 可以免费游玩.")
elif int(input("请告诉我今天几号: ")) == 1:
    print("今天是1号免费日, 可以免费游玩.")
else:
    print("不好意思, 条件都不满足, 需要买票10元.")
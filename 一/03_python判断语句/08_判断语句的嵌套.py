"""
演示判断语句的嵌套使用
"""

# if int(input("你的身高是多少: ")) > 120:
#     print("身高超出限制, 不能免费.")
#     print("但是, 如果VIP级别大于3, 可以免费.")
#
#     if int(input("你的VIP级别是多少: ")) > 3:
#         print("VIP等级达标, 可以免费.")
#     else:
#         print("你需要买票10元.")
# else:
#     print("欢迎小朋友, 免费游玩.")

age = int(input("请输入你的年龄: "))
if age >= 18:
    if age <30:
        print("年龄达标.")
        if int(input("请输入你的入职时间: ")) > 2:
            print("入职时间达标, 可以领取礼物.")
        elif int(input("请输入你的级别: ")) > 3:
            print("级别大于3, 可以领取礼物.")
        else:
            print("入职时间不大于两年且级别不大于3, 不能领礼物.")
    else:
        print("年龄大于30.")
else:
    print("未成年.")
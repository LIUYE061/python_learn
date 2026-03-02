"""
break 和 continue
"""

# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句一")
#     continue
#     print("语句二")

# 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句一")
#     for j in range(1, 6):
#         print("语句二")
#         continue
#         print("语句三")
#
#     print("语句四")

# 演示循环中断语句 break
# for i in range(1, 101):
#     print("语句一")
#     break
#     print("语句二")
#
# print("语句三")

# 演示break的嵌套应用
for i in range(1, 6):
    print("语句一")
    for j in range(1, 101):
        print("语句二")
        break
        print("语句三")

    print("语句四")
"""
演示捕获异常
"""

# # 基本捕获语法
# try:
#     f = open("abc.txt", "r", encoding="utf-8")
# except:
#     print("出现异常了, 因为文件不存在, 改为w模式去打开")
#     f = open("abc.txt", "w", encoding="utf-8")
#
# # 捕获指定的异常
# try:
#     print(name)
#     # 1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常")
#
# # 捕获多个异常
# try:
#     # print(1 / 0)
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除以0的异常")

# 未正确设置捕获异常类型, 将无法捕获异常


# 捕获所有异常
try:
    # 1
    # 1 / 0
    # print(name)
    f = open("abc.txt", "r", encoding="utf-8")
except Exception as e:
    # print(e)
    f = open("abc.txt", "w", encoding="utf-8")
else:
    print("没有异常")
finally:
    f.close()
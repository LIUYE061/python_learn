"""
演示对文件的读取
"""
import time

# 打开文件
f = open("C:/test.txt", "r", encoding = "UTF-8")
print(type(f))

# 读取文件 - read()
# print(f.read(10))
# print(f.read())

# 读取文件 - readlines()
# lines = f.readlines()
# print(lines, type(lines))

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1, type(line1))
# print(line2)
# print(line3)

# for循环读取文件行
for line in f:
    print(line)

# 文件的关闭
# time.sleep(200000)
f.close()

# with open 语法操作文件
with open("c:/test.txt", "r") as f:
    for line in f:
        print(line)
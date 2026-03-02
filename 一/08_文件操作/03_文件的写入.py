"""
演示文件的写入
"""

import time

# 打开文件, 不存在的文件
# f = open("test.txt", "w", encoding="utf-8")

# write写入
# f.write("hello world")

# flush刷新
# f.flush()

# close关闭
# f.close()

# 打开一个存在的文件
f = open("test.txt", "w", encoding="utf-8")

# write写入, flush刷新
f.write("itheima")

# close关闭
f.close()
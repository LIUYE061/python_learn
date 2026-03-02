"""
演示文件的追加写入
"""

# 打开文件, 不存在的文件
# f = open("test.txt", "a", encoding = "utf-8")

# write写入
# f.write("itheima")

# flush刷新
# f.flush()

# close关闭
# f.close()

# 打开一个存在的文件
f = open("test.txt", "a", encoding = "utf-8")

# write写入, flush刷新
f.write("学python")
f.flush()

# close关闭
f.close()
"""
案例: 文件备份

读取文件
将文件写出到bill.txt.bak文件作为备份
同时, 将文件内标记为测试的数据行丢弃
"""

with open("bill.txt", "r", encoding = "utf-8") as f:
    f1 = open("bill.txt.bak", "a", encoding="utf-8")
    for line in f:
        flag = line.count("测试")
        if not flag:
            f1.write(line)
    f1.close()

# 总结: f1用w模式即可, 因为前面写入的所有虽然不是一次写入, 但都在缓冲区, 最后close才一次性全部写入
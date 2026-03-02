"""
01课后练习: 单词计数
"""

with open("c:/word.txt", "r") as f:
    # 1
    # content = f.read()
    # print(content.count("itheima"))

    # 2
    count = 0
    for line in f:
    #     num = line.replace("\n", " ").split(" ").count("itheima")
        num = line.strip("\n").split(" ").count("itheima")
        count += num
    print(count)
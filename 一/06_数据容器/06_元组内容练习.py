"""
元组练习案例
"""

# 定义元组
t1 = ("周杰轮", 11, ["football", "music"])

# 查询年龄的下标
print(f"年龄的下标为{t1.index(11)}")

# 查询学生姓名
print(f"学生姓名: {t1[0]}")

# 删除学生爱好中的football
t1[2].pop(0) # 或 del t1[2][0]
print(t1)

# 增加爱好: coding到爱好list内
t1[2].insert(0, "coding")
print(t1)
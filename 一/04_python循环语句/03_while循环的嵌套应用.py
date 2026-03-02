"""
演示while循环的嵌套使用
"""

# 100天
# 每天10次
i = 1
while i <= 100:
    print(f"第{i}天")
    j = 1
    while j <= 10:
        print(f"第{j}次")
        j += 1
    i += 1
"""
演示字符串的三种定义方式
- 单引号定义法
- 双引号定义法
- 三引号定义法
"""

# 单引号
name = 'string'
print(type(name))
# 双引号
name = "string"
print(type(name))
#三引号
name = """
str
ing
"""
print(type(name))

# 在字符串内包含双引号
name = '"string"'
print(name)
# 包含单引号
name = "'string'"
print(name)
# 使用转义字符
name = "\"string\""
print(name)
name = '\'string\''
print(name)

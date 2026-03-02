# 方式一: 使用print直接输出类型信息
print(type("字符串"))
print(type(666))
print(type(13.14))

# 方式二:  使用变量存储type()语句的结果
string_type = type("字符串")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 方式三:  使用type()语句,查看变量中存储的数据类型信息
name = "字符串"
name_type = type(name)
print(name_type)
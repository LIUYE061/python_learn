# 规则1: 内容限定
# 1_name = "张三"  数字开头
# name_! = "张三"  范围外的内容
name_ = "张三"
_name = "张三"
name_1 = "张三"

# 规则2: 大小写敏感
Liuye = "六也"
liuye = 666
print(Liuye)
print(liuye)

# 规则3: 不能使用关键字
# class = 1  使用了关键字
# def = 1  同上
Class = 1  #关键字同样大小写敏感
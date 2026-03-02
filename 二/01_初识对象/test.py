# 1.设计一个类
class Student:
    name = None            # 记录学生姓名
    gender = None          # 性别
    nationality = None     # 国籍
    native_place = None    # 籍贯
    age = None             # 年龄

# 2.创建一个对象
stu1 = Student()

# 3.对象属性进行赋值
stu1.name = "小明"
stu1.gender = "男"
stu1.nationality = "china"
stu1.native_place = "henan"
stu1.age = 31

# 4.获取对象中记录的信息
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)
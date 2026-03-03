"""
演示面向对象类中的成员方法定义和使用
"""

# 定义一个带有成员方法的类
class Student:
    name = None        # 姓名
    age = None         # 年龄

    def say_hi(self):
        print(f"大家好, 我是{self.name}, {self.age}岁")

    def say_hi2(self, msg):
        print(f"大家好, 我是{self.name}, {msg}")

stu1 = Student()
stu1.name = "xiaoming"
stu1.age = 21
stu1.say_hi2("111")

stu2 = Student()
stu2.name = "xiao"
stu2.age = 23
stu2.say_hi2("222")
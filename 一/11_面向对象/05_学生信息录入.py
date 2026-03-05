"""
for循环, 配合input, 使用构造方法, 完成学生信息的键盘录入
输入完成后, print输出信息
"""

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

student_list = []

num = 10

for i in range(1, num):
    print(f"当前录入第{i}位学生信息, 总共需录入10位学生信息")
    name = input("请输入学生姓名: ")
    age = input("请输入学生年龄: ")
    address = input("请输入学生地址: ")
    student_list.append(Student(name, age, address))
    print(f"学生{i}信息录入完成, 信息为: 学生姓名: {name}, 年龄: {age}, 地址: {address}")

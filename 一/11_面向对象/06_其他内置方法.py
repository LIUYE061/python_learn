class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象, name:{self.name}, age: {self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("小明", 31)
print(stu1)
print(str(stu1))

stu2 = Student("小红", 23)
print(stu1 < stu2)
print(stu1 > stu2)

print(stu1 <= stu2)
print(stu1 >= stu2)

print(stu1 == stu2)

class Person:

    def __new__(cls, name, age):
        print("__new__方法")
        return object.__new__(cls)

    def __init__(self, name, age):
        print("__init__方法")
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__方法")

    def __str__(self):
        return "LY"

# del情况一
# p1 = Person('张三', 29)
# print("最后一行代码")      # 最后一行代码
                        # __del__方法

# del情况二
# p1 = Person('张三', 29)
# del p1                      # __del__方法
# print("最后一行代码")         # 最后一行代码

# del情况三
p1 = Person('张三', 29)
# p2 = p1
# del p1
# print("最后一行代码")         # 最后一行代码
# __del__方法

print(p1)
print(str(p1) + "_")
print(f'{p1}_061')

"""
演示类和对象的关系, 即面向对象的编程套路(思想)
"""

import winsound

# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        winsound.Beep(2000, 3000)

# 构建两个闹钟对象并让其工作
clock1 = Clock()
clock1.id = 2001
clock1.price = 100
clock1.ring()

clock2 = Clock()
clock2.id = 2002
clock2.price = 100
clock2.ring()
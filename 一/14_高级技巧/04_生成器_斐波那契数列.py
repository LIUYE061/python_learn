"""
用迭代器生成斐波那契数列
"""

def fib(n):
    count, a, b = 0, 0, 1
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fib(20):
    print(num)
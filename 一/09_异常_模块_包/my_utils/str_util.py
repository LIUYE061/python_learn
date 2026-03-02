"""
字符串工具
"""

def str_reverse(s):
    """
    接受传入字符串, 将字符串反转返回
    :param s: 传入字符串
    :return: 反转s
    """
    s1 = ""
    for ch in s:
        s1 = ch + s1
    return s1

def substr(s, x, y):
    """
    按照下标x和y, 对字符串进行切片
    :param s: 传入字符串
    :param x: 切片起始下标
    :param y: 切片结束下标
    :return: 切片后字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello world", 1, 3))
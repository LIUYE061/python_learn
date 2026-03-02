"""
演示对list列表的循环, 使用while和for循环2种方式
"""

# def list_while_func():
#     """
#     使用while循环遍历列表
#     :return: None
#     """
#     mylist = ["a", "b", "c"]
#     index = 0
#     while index < len(mylist):
#         print(mylist[index])
#         index += 1
#
# def list_for_func():
#     """
#     使用for循环遍历列表
#     :return: None
#     """
#     mylist = ["a", "b", "c"]
#     for element in mylist:
#         print(element)
#
# list_while_func()
# list_for_func()

def list_while_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mylist2 = []
    index = 0
    while index < len(mylist):
        if mylist[index] % 2 ==0:
            mylist2.append(mylist[index])
        index += 1
    print(mylist2)

# list_while_func()

def list_for_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mylist2 = []
    for element in mylist:
        if element % 2 == 0:
            mylist2.append(element)
    print(mylist2)

list_for_func()
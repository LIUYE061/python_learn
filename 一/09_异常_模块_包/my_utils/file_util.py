"""
文件处理工具
"""

def print_file_info(file_name):
    """
    接受传入文件的路径, 打印文件的全部内容,
    如文件不存在则捕获异常, 输出提示信息, 通过finally关闭文件对象
    :param file_name: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, mode = "r", encoding = "utf-8")
    except FileNotFoundError as e:
        print(e)
    else:
        for line in f.readlines():
            print(line)
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    接受文件路径及传入数据, 将数据追加写入到文件中
    :param file_name: 文件路径
    :param data: 数据
    :return: None
    """
    f = open(file_name, mode = "a", encoding = "utf-8")
    f.write(data)
    f.close()

if __name__ == '__main__':
    print_file_info("py1.txt")
    append_to_file("py1.txt", "1")
"""
完成案例: ATM
"""

# 全局变量money(默认值), name(启动程序时输入)
money = 5000000
name = None
move = 0

# 要求用户输入名字
name = input("请输入您的名字: ")


# 余额查询函数
def select():
    print(f"当前余额: {money}")
    menu()

# 存款函数
def save():
    save_money = int(input("请输入存款金额: "))
    global money
    money += save_money
    print(f"存款成功, 当前余额: {money}")
    menu()

# 取款函数
def get():
    get_money = int(input("请输入取款金额: "))
    global money
    if money >= get_money:
        money -= get_money
        print(f"取款成功, 当前余额: {money}")
    else:
        print(f"余额不足, 当前余额: {money}")
    menu()

# 主菜单函数
def menu():
    print("---------- ----主菜单---------------")
    print(f"{name}, 您好, 欢迎来到ATM. 请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    global move
    move = int(input("请输入您的选择: "))

# 主体
    if move == 1:
        select()
    elif move == 2:
        save()
    elif move == 3:
        get()
    else:
        print("退出成功")

menu()
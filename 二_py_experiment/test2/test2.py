# # 问题一  学生信息管理系统
#
# students = []
#
# # 功能菜单
# def enter_menu():
#     while True:
#         print("=================================")
#         print("学生管理系统 V10.10")
#         print("1.添加学生信息")
#         print("2.删除学生信息")
#         print("3.修改学生信息")
#         print("4.查询所有学生信息")
#         print("0.退出系统")
#         print("=================================")
#         choice = int(input("请输入操作序号: "))
#
#         if choice == 1:
#             add_stu()
#         elif choice == 2:
#             del_stu()
#         elif choice == 3:
#             modify_stu()
#         elif choice == 4:
#             print_stu()
#         elif choice == 0:
#             print('感谢使用学生管理系统, 再见!')
#             break
#
# # 添加学生信息
# def add_stu():
#     stu = {}
#     stu['name'] = input("请输入学生姓名: ")
#     stu['gender'] = input('请输入学生性别: ')
#     stu['phone'] = input('请输入学生手机号: ')
#     students.append(stu)
#     print('添加成功!')
#
# # 删除学生信息
# def del_stu():
#     if not students:
#         print("学生信息表为空, 无法删除数据!")
#         return
#     del_index = int(input('请输入删除学生序号: '))
#     if 1 <= del_index <= len(students):
#         del students[del_index - 1]
#     print('删除成功!')
#
# # 修改学生信息
# def modify_stu():
#     if not students:
#         print('学生信息表为空, 无法修改数据!')
#         return
#     stu = {}
#     modify_index = int(input('请输入修改学生序号: '))
#     if 1 <= modify_index <= len(students):
#         stu['name'] = input('请输入修改后学生姓名: ')
#         stu['gender'] = input('请输入修改后学生性别: ')
#         stu['phone'] = input('请输入修改后学生手机号: ')
#         students[modify_index - 1] = stu
#
# # 查询所有学生信息
# def print_stu():
#     if not students:
#         print('学生信息表为空!')
#         return
#     print('序号\t\t姓名\t\t性别\t\t手机号\t\t')
#     for idx, stu in enumerate(students, start=1):
#         print(f'{idx}\t\t{stu["name"]}\t\t{stu["gender"]}\t\t{stu["phone"]}')
#
# enter_menu()




# # 问题二
#
# # 求阶乘
# def f(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# sum = 0
# for i in range(1, 11):
#     sum += f(i)
# print(sum)



# # 问题三  两数范围内素数的个数
#
# # 素数判断
# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# x = int(input('请输入第一个数: '))
# y = int(input('请输入第二个数: '))
# sum = 0
# for i in range(x, y + 1):
#     if is_prime(i):
#         sum += 1
# print(sum)




# # 问题四  既是回文数又是素数
#
# # 回文数判断   反转判断
# def h(n: int) -> bool:
#     n = str(n)
#     if n == n[::-1]:
#         return True
#     return False
#
# for i in range(100, 1000):
#     if is_prime(i) and h(i):
#         print(i)



# 问题五  画出奥运五环图
# 导入Python内置的turtle绘图库
import turtle

# ========== 绘图基础设置 ==========
# 设置画布窗口大小，适配五环展示
turtle.setup(width=800, height=600)
# 设置窗口标题
turtle.title("奥运五环")
# 设置画笔粗细（匹配五环的环宽效果）
turtle.pensize(10)
# 设置绘画速度（5为适中速度，0为最快速度）
turtle.speed(5)

# ========== 定义画环通用函数（避免重复代码） ==========
def draw_ring(x, y, ring_color):
    """
    绘制单个奥运五环圆环
    :param x: 圆环圆心的X轴坐标
    :param y: 圆环圆心的Y轴坐标
    :param ring_color: 圆环的颜色
    """
    turtle.penup()               # 抬笔，移动时不留下轨迹
    turtle.goto(x, y - 80)       # 移动到圆的底部（圆心(x,y)，半径80）
    turtle.pendown()             # 落笔，开始绘制
    turtle.color(ring_color)     # 设置画笔颜色
    turtle.circle(80)            # 绘制半径为80的正圆

# ========== 按顺序绘制五环 ==========
# 上排三环：左蓝、中黑、右红（标准奥运配色）
draw_ring(-180, 0, "#0085C7")
draw_ring(0, 0, "#000000")
draw_ring(180, 0, "#DF0024")

# 下排二环：左黄、右绿（标准奥运配色，与上环形成套接效果）
draw_ring(-90, -80, "#FDB913")
draw_ring(90, -80, "#009E49")

# ========== 绘制收尾设置 ==========
turtle.hideturtle()  # 隐藏画笔箭头，让画面更整洁
turtle.done()        # 保持绘图窗口，不会绘制完成后自动关闭
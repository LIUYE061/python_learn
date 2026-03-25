
# q1: 计算BMI指数    体重(kg)/身高(m)**2
# weight = float(input("请输入您的体重(kg):"))
# height = float(input("请输入您的身高(m):"))
# BMI = weight / (height * height)
#
# print(f"您的BMI指数为: {BMI}")

# q2: 词频统计
# s = input("请输入一段英文内容")
# s1 = s.lower()
# my_dict = {}
#
# for s in s1:
#     if s in my_dict:
#         my_dict[s] += 1
#     else:
#         my_dict[s] = 1
#
# print(my_dict)

# q3: 成语接龙
# li = ["万事如意", "发奋图强", "笑容满面", "意气风发", "强颜欢笑"]
# index = 0
#
# while li:
#     if index is None:
#          print("未找到可接龙成语")
#          break
#     s = li.pop(index)
#     index = None
#     print(s)
#     for i in range(len(li)):
#         if s[-1] == li[i][0]:
#             index = i
#             break

# q4: 房贷计算器
# loan_type = int(input("请选择您的贷款类型:(商业贷款输入0, 公积金贷款输入1)"))
# loan_money = int(input("请选择您的贷款金额:(元)"))
# loan_data = int(input("请选择您的贷款期限:(年)"))
#
# if loan_type == 0:
#     if loan_data <= 5:
#         rate = 0.0475
#         yuegong = loan_money * (rate / 12) * ((1 + rate / 12) ** (loan_data * 12)) / ((1 + rate / 12) ** (loan_data * 12) - 1)
#     else:
#         rate = 0.049
#         yuegong = loan_money * (rate / 12) * ((1 + rate / 12) ** (loan_data * 12)) / ((1 + rate / 12) ** (loan_data * 12) - 1)
# else:
#     if loan_data <= 5:
#         rate = 0.026
#         yuegong = loan_money * (rate / 12) * ((1 + rate / 12) ** (loan_data * 12)) / ((1 + rate / 12) ** (loan_data * 12) - 1)
#     else:
#         rate = 0.031
#         yuegong = loan_money * (rate / 12) * ((1 + rate / 12) ** (loan_data * 12)) / ((1 + rate / 12) ** (loan_data * 12) - 1)
#
# repayment = yuegong * loan_data * 12
# accrual = repayment - loan_money
#
# print(f"每月月供参考: {yuegong:,.2f}, 还款总额: {repayment:,.2f}, 支付利息: {accrual:,.2f}")

# q5: 中文数字对照表
# cn_digits = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
# s = ""
# num = input("请输入一个数字:")
#
# for i in num:
#     index = int(i)
#     s += cn_digits[index]
#
# print(s)

# q6: 圆周率
def arctan(x, terms=10):
    """计算反正切 arctan(x) 的泰勒展开"""
    result = 0
    x_squared = x * x
    numerator = x  # 分子：x, x^3, x^5...
    denominator = 1
    sign = 1

    for _ in range(terms):
        result += sign * numerator / denominator
        numerator *= x_squared  # 每次多乘 x^2
        denominator += 2
        sign *= -1
    return result


def machin_pi(terms=20):
    """使用马青公式计算 π"""
    part1 = 4 * arctan(1 / 5, terms)
    part2 = arctan(1 / 239, terms)
    return 4 * (part1 - part2)


# 测试：只需要很少的项就能达到很高精度
pi_estimate = machin_pi(10)
print(f"马青公式估算 π:   {pi_estimate}")
print(f"Python 内置的 π:   {3.141592653589793}")
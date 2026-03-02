"""
练习案例: 序列的切片实践
"""

my_str = "万过薪月, 员序程马黑来, nohtyp学"
new_str = ""
index = len(my_str)
while index > 0:
    new_str += my_str[index-1]
    index -= 1
print(new_str[10:15:1])

print(my_str[10:5:-1])

new_list = my_str.split(",")
str1 = new_list[1]
str2 = str1.replace("来", "")
print(str2[::-1])
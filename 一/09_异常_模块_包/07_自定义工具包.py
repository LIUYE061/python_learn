"""
使用自定义工具包 my_utils
"""

from my_utils import str_util
from my_utils import file_util

s = "abc123"
print(str_util.str_reverse(s))
print(str_util.substr(s, 0, 4))

file_name = "py1.txt"
file_util.print_file_info(file_name)
file_util.append_to_file(file_name, s)
"""
演示python的模块导入
"""

# 使用import导入time模块使用sleep功能(函数)
# import time

# time.sleep(5)

# 使用from导入time的sleep功能
# from time import sleep

# sleep(5)

# 使用 * 导入time模块的全部功能
# from time import *

# sleep(5)

# 使用as给特定功能加上别名
# import time as t

# t.sleep(5)

from time import sleep as sl

sl(5)
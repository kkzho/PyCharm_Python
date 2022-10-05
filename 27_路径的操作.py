
# 相对路径
# 绝对路径

import os
print(os.getcwd())          #获取当前路径
print(os.path.abspath('27_路径的操作.py'))    #返回文件的/绝对路径/
print(os.path.dirname(r'/Users/fan.zhou/Documents/PyCharm CE'))
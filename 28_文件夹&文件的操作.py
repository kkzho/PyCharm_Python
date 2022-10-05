
import os

# os.makedirs('工作文件夹')    #创建文件夹
# os.rmdir('工作文件夹')       #删除

f = open('text.py','w')     # 创建文件,读写(w) 追加(a) 读取(r)
f.write('Hello Python\n')   # \n 换行
f.write('abc\n')
f.write('12138\n')
f.close()                   # 关闭文件

# 优化自动关闭功能
with open('text.py','a') as f: #将open功能赋值f
    f.write('Hello Python\n')  # \n 换行
    f.write('abc\n')
    f.write('12138\n')         #完成自动关闭



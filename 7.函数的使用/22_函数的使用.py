
#
def fun1(info1,info2):                      # 定义函数fun1(包含2参数)
    print(f'如果{info1}在,{info2}会幸福嘛?')  # 输出结果
fun1("典典","我们")                          # 传入2变量

# 传递多个参数(可变参数)
def fun2(*args)             # __*args 可变参数

def fun3(**kwargs):
    print(f'请大家给我{info1},{info2},{info3}')

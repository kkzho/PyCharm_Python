# 逻辑运算符: { and  or  not }__返回 " True/False "

a = 1
b = 2
c = 3
# and: 有一个表达式False,即返回False
print( a > b and b > c )    # False
print( c > b and b > a )    # True
print('===============')
# or
print( a>b or c>b )         # T
print('===============')
# not
print(not True)
print(not a>b)  # a>b:为False,故not返回:True
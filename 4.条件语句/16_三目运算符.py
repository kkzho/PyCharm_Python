
point = 3

if point == 3:
    rs = '一键三连~'
else:
    rs = '请多多投币喔!'
print(rs)

# 方法2: 三目运算符
point = 4
print('一键三连~' if point == 3 else '请多多投币喔!') # true返回值,if判断;False返回值(else👉)
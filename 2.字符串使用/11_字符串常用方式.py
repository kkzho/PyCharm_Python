
# 查找 判断 修改
info = 'hello python and world and 周二凡'

# find index count
print('='*10,'find','='*10)
print(info.find('and'))
print(info.find('and',15,30))   # find('字符',起始位置,结束位置)
print(info.find('ands'))        # 未找到返回-1

print('='*10,'index','='*10)
print(info.index('and'))
print(info.index('and',15,30))
print(info.index('and'))
# print(info.index('ands'))     # 未找到会'报错'

print('='*10,'count','='*10)
print(info.count('and'))
print(info.count('and',15,30))
print(info.count('ands'))

# 修改
print(info.upper())
print(info.lower())
print(info.title())             # title() 单词_首字母大写
print(info.capitalize())        # capitalize() 句首大写

# 替换
print('='*10,'replace','='*10)
print(info.replace('and','add'))# and 全换成 add
print(info.replace('and','add',1))# 替换第一个and,为:add

# 分隔
print('='*10,'split','='*10)
print(info.split())             # 默认[空格]分隔'字符'
print(info.split('and'))        # 以填入'字符'分隔

# 拼接
print('='*10,'join','='*10)
tmp = info.split()
print(tmp)
print(''.join(tmp))            # 以''拼接
#['hello', 'python', 'and', 'world', 'and', '周二凡']->零间隔合并

# 去除[空格]
print('='*10,'strip','='*10)
info2 = '   i love python    '
print(info2.strip())           # strip():去除两端[空格]
print(info2.lstrip())          # strip():去除左[空格]
print(info2.rstrip())          # strip():去除右[空格]

# startswith endswith 判断是否为指定字符 ——开头
print('='*10,'startswith','='*10)
print(info.startswith('python'))# False
print(info.endswith('周二凡'))   # True

# 判断字符串类型:
print('='*10,'is__','='*10)
info3 = '123'
info4 = 'abc'
info5 = 'abc123'
info6 = 'abc_'
print(info3.isdigit())  # 数字
print(info4.isalpha())  # 字母
print(info5.isalnum())  # 数字+字母

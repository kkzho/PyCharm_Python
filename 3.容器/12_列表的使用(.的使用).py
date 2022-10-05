
# append: 插入单个'字符'
print('================ append ================')
name_list = ['周凡','二凡','典典']
print(name_list)
name_list.append('文博')
print(name_list)

# extend: 多个字符添加
print('================ extend ================')
name_list1 = ['周凡','二凡','典典']
name_list1.extend(['文博','dd'])   # []引住
print(name_list1)

# insert: 定位插入
print('================ insert ================')
name_list2 = ['周凡','二凡','典典']
name_list2.insert(1,'wk')   # 位置[1]上,插入'wk'
print(name_list2)

# del: 删除
print('================ del ================')
name_list3 = ['周凡','二凡','典典']
del name_list3[1]          # 删除位置[1]的'二凡'
print(name_list3)

# 剪切--'列表中元素'
print('================ pop ================')
name_list4 = ['周凡','二凡','典典']
tmp = name_list4.pop()
print(tmp)          # 默认剪切末位:'典典'
print(name_list4)   # 列表剩余:   ['周凡', '二凡']
#   tmp = name_list4.pop(1) #剪切[1]:     '二凡'
#   print(name_list4)       # 列表剩余:   ['周凡', '典典']

# remove:移除'元素'
print('================ remove ================')
name_list5 = ['周凡','二凡','典典']
name_list5.remove('二凡')
print(name_list5)

# clear: #清空列表
print('================ clear ================')
name_list6 = ['周凡','二凡','典典']
print(name_list6)
name_list6.clear()      # name_list6变为: 空列表[]
print(name_list6)

print('================ 修改 ================')
name_list7 = ['周凡','二凡','典典']
name_list7[0] = 'Wiki'  # 将[0]位元素替换为:'Wiki'
print(name_list7)

# reverse:倒序输出
print('================ reverse ================')
name_list8 = ['周凡','二凡','典典']
name_list8.reverse()
print(name_list8)

# sort:元素「排序」
print('================ sort ================')
name_list9 = ['周凡','二凡','典典']
name_list9.sort()
print(name_list9)

print('================ in ================')
name_list10 = ['周凡','二凡','典典']
print('love' in name_list10)   # False
print('典典' in name_list10)    # True

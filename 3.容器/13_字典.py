
# 创建字典的三种方式:
dict1 = {}
dict2 = dict()
dict3 = {'name':'周二凡','from':'shanghai','date':'2022-06-19'}
        # {键:值,}

# 增加:
print('================ 字典(增加) ================')
dict1['name'] = '典典'
print(dict1)            # {'name': '典典'}
dict1['name'] = 'wiki'
print(dict1)            # {'name': 'wiki'} 替换掉原有数据

# 获取(字典内容)
print('================ 获取内容 ================')
print(dict1.get('age')) # 无对应key:返回'none' (优先使用!!!)
# print(dict1['age'])     # 无索引值报错!

print(dict3.keys())
# dict_keys(['name', 'from', 'date'])               --返回key
print(dict3.values())
# dict_values(['周二凡', 'shanghai', '2022-06-19'])  --返回'值'

# del:删除
print('================ del删除 ================')
dict1['name'] = '典典'
del dict1['name']
print(dict1)
# {}

dict3.clear()
print(dict3)   # 全部清空

# 字典生成式: zip()
items=['Fruits','Books','Others']
prices=[96,78,85,100,902]
d = {item:price for item,price in zip(items,prices)} #设置{字典d}
print(d)    # {'Fruits': 96, 'Books': 78, 'Others': 85} ###逐一匹配

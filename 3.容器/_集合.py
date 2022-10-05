
'''1. 集合_创建方式(集合=字典"值")'''
# {}创建
s={2,3,4,5,5,6,7,7}
print(s)    #集合:无重复项

# set()创建
s1=set(range(6))
print(s1,type(s1))  # {0, 1, 2, 3, 4, 5} <class 'set'>
s2=set('Python')
print(s2)  # {'n', 't', 'o', 'h', 'P', 'y'} --无序性


'''2. 集合_相关操作'''
# 判断操作: in 或 not in
s={10,20,50,102,99}
print(10 in s and 0 not in s)  #True

# 新增操作: .add(单一元素) / .update(多个元素)
s.add(0)    # {0, 50, 99, 20, 102, 10}: add新增'0'
print(s)
s.update([11],{1,2,3},(56,42)) # 插入:{},[],()任意格式
print(s)    # {0, 1, 2, 99, 3, 102, 10, 11, 42, 50, 20, 56}

# 删除操作:
# .remove(单一)/.duscard(单一):删除不报错/.pop(随机删除)/.clear(清空)
s.remove(0) # 删除0
print(s)
s.pop() #随机删一个元素
print(s)
s.clear()
print(s)    # set():剩余空集合

'''3. 集合_数学操作'''
s1={1,2,3}
s2={1,7,9}
# 交集: .intersection() / &:交集
print(s1.intersection(s2))  # 交集:{1}
print(s1 & s2)

# 并集: .union() / |
print(s1 .union(s2))
print(s1 | s2)  # {1, 2, 3, 7, 9}

# 差集: .difference() / -
print(s1-s2) # {1,2,3} - {1,7,9} = {2, 3}

# 对称差集: .symmetric_difference() / ^
print(s1.symmetric_difference(s2))
print(s1 ^ s2)  # 非交集: {2, 3, 7, 9}

'''4. 集合间的关系:'''
s={1,3,5,7,9}
s2={1,101}
s3={3,5}
    # 子集 .issubset()
print(s2.issubset(s))   #False: s2.101不包含s中
print(s3.issubset(s))   #True

    # 超集(父) .issuperset()
print(s.issuperset(s3)) # s为父集

    # 交集 .is
print('s2,s3是否有交集:',s2.isdisjoint(s3))
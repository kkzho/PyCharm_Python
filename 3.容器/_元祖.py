#元祖的创建方式:
t1=('Py','exc',1)          # 1. ('',)
t2=tuple( ('Python','world',2) ) # 2. tuple( ('',) )
t3=(10,)    #元祖存放: int,[list],'str'
print(t1,type(t2))
print(t2,type(t2))
print(t3,type(t3))
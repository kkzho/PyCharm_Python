
# range()的三种创建方式:
''' 1. range(10): 默认0~stop '''
r=range(10)
print(list(r))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

''' 2. range(2,10): begin~stop '''
r=range(2,10)
print(list(r))  #[2, 3, 4, 5, 6, 7, 8, 9]

''' 3. range(1,10,2): 起始1~结束9(步长为2) '''
r=range(1,10,2)
print(list(r))  #[1, 3, 5, 7, 9]
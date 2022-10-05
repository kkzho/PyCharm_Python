infos = [
    ['z','h','o','u'],
    ['F','A','N'],
    ['w','u','kai','love']
]

#方法1:
count = 1
for info in infos:
    print(f'============第{count}个============')
    count += 1
    for i in info:
        print(i)

#方法2:
for i in range(len(infos)):
    for info in infos[i]:
        print(info)

#方法3:
for i,info in enumerate(infos):            # i: 0,1,2
    print(f'=======周{i+1}的内容======')    # info:取第i位数组
    for tmp in info:
        print(tmp)

# 打印一个3行4列矩形
for i in range(1,4):        #[1,2,3]控制行数
    for j in range(1,5):    #[1,2,3,4]控制列
        print('*',end='\t') #输出*,\t:空格
    print()                 #列循环一遍,换行

# 打印九九乘法表
'''
公式:
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='\t')
    print()
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    print()
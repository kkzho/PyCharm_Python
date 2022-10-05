
# while语句:
i = 0
while i<5:
    print('努力工作!')
    i += 1
print('任务结束')

print('================')

# eg_1: 1 到100累加和:
i = 1
rs = 0          # rs 作'累加容器'

while i <= 100:
    rs += i     # rs=rs+i
    i += 1
print(f'1-100间的累加和是:{rs}')          #print(f'  {x}')
print('1-100间的累加和是:%d'%rs)          #print('  ')
print('1-100间的累加和是:{}'.format(rs))  #print(' {}'.format(x))

# eg_2: 计算0～100的偶数和:
sum=0
a=1
while a<=100:
    if not bool(a%2):   #整数= a%2余数为:0 ; not bool(0)=True
        sum+=a
    a+=1
print('0~100的偶数和为:{}'.format(sum))

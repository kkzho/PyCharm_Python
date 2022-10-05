
# 例1
print('典典,陪你逛街去买包～')
i = 1                                # 定义变量i
while True:
    if i == 5:
        print('这个包不错,买它～')     # end result
        break                       # 强制推出'死循环'
    print('这家不行,再换一家')        # ♻️输出
    i += 1                          #

# 例2

from random import randint # start,end
for i in range(8):
    num = randint(3,8)
    print(f'========第i位 评分是:{num}==========')
    print('点赞')
    if num <6:
        continue                    # continue进入下次循环
    print('收藏')
    print('投币')
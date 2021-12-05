'''
Author: your name
Date: 2021-04-26 21:32:05
LastEditTime: 2021-07-14 13:21:27
LastEditors: your name
Description: In User Settings Edit
FilePath: /python study/抽奖.py
'''
import random
import time
m=0
b=[]
def choujiang(*name):
    luckylist=name
    a=random.choice(luckylist)
    print('开奖倒计时')
    time.sleep(1.5)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('恭喜{}中奖'.format(a))
while True:
    answer=input('是否有人参加\n Y or N\n')
    if answer=='Y':
        m=m+1
        b.append(input('请输入参加抽奖的第{}个人:'.format(m)))
    if answer=='N':
        c=tuple(b)
        choujiang(*c)
        break
print('抽奖结束')


import time
import random
E=0
F=0
N=1
list1=[]
while 1:
    if E+F>=3 or E>=2 or F>=2:
        again=input('是否继续游戏？\n A.Yes B.No\n')
        if again=='B':
            break
    print('第'+str(N)+'局')
    print('--------------------------------')
    time.sleep(1.5)
    N=N+1
    A=random.randint(100,150)
    B=random.randint(100,150)
    C=random.randint(30,50)
    D=random.randint(30,50)
    print('【玩家】\n血量：{}攻击力：{}'.format(A,C))
    print('--------------------------------')
    time.sleep(1.5)
    print('【玩家】\n血量：{}攻击力：{}'.format(B,D))
    print('--------------------------------')
    while 1:  
        time.sleep(1.5)
        B=B-C
        if B>0:
            print('你发起了攻击，【对手】血量：'+str(B))
        else:
            print('你发起了攻击，【对手】血量：'+str(B))
            print('你赢了！')
            E=E+1
            list1.append('赢')
            break
        print('--------------------------------')
        time.sleep(1.5)
        A=A-D
        if A>0:
            print('对手发起了攻击，【玩家】血量：'+str(A))
        else:
            print('对手发起了攻击，【玩家】血量：'+str(A))
            print('你死了。')
            F=F+1
            list1.append('输')
            break
        print('--------------------------------')
print('您的战果为'+str(list1))
if E>F:
    print('--------------------------------')
    time.sleep(1.5)
    print('您获胜了！')   
if F>E:
    print('--------------------------------')
    time.sleep(1.5)
    print('您失败了。')
if F==E:
    print('--------------------------------')
    time.sleep(1.5)
    print('平局')
print('--------------------------------')
time.sleep(1.5)
print('游戏结束')
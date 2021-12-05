import random
import time
#角色生成
player_list=['【齐天大圣】','【杨戬】','【唐僧】','【猪八戒】','【哪吒】','【雷震子】']
enemy_list=['【蝎子精】','【黑·悟空】','【黑熊精】','【蜘蛛精】','【六耳猕猴】','【白骨精】']
player=random.sample(player_list,3)
enemy=random.sample(enemy_list,3)
player_all={}
enemy_all={}
def player_data():
    player_life=random.randint(100,150)
    player_attack=random.randint(30,50)
    return player_life,player_attack
def enemy_data():
    enemy_life=random.randint(100,150)
    enemy_attack=random.randint(30,50)
    return enemy_life,enemy_attack
for i in range(3):
        player_all[player[i]]=player_data()
        enemy_all[enemy[i]]=enemy_data()   
#展示角色
def shou_role(j):
        print('{}血量：{} 攻击力：{}'.format(player[j],player_all[player[j]][0],player_all[player[j]][1]))
        print('------------------------------')
        time.sleep(1.5)
        print('{}血量：{} 攻击力：{}'.format(enemy[j],enemy_all[enemy[j]][0],enemy_all[enemy[j]][1]))
        print('------------------------------')
        time.sleep(1.5)
#双方pk
def pk(k,j):
    score=0
    player_life=player_all[player[k]][0]
    enemy_life=enemy_all[enemy[j]][0]
    while player_life>0 and enemy_life>0:
        player_life= player_life-enemy_all[enemy[j]][1]
        enemy_life=enemy_life-player_all[player[k]][1]
        print('你发起了攻击，【敌人】剩余血量：{}'.format(player_life))
        print('敌人发起了攻击，【敌人】剩余血量：{}'.format(enemy_life))
        print('------------------------------')
        time.sleep(1.5)
    if player_life>0 and enemy_life<=0:
        print('你赢了！')
        score=score+1
    elif player_life<=0 and enemy_life>0:
        print('你输了。')
        score=score-1
    else:
        print('你们同归于尽了。')
    print('------------------------------')
    time.sleep(1.5)
    H=input('按回车以继续\n')
    if H=='\n':
        pass
    return score
#战斗结果   
def main():
    for i in range(3):
        shou_role(i)
    answer1=input('我方阵容：1.{} 2.{} 3.{}\n敌方阵容：1.{} 2.{} 3.{}\n是否更改出场顺序？'.format(player[0],player[1],player[2],enemy[0],enemy[1],enemy[2]))
    if answer1=='是':
        answer2=input('请输入您的出场顺序')
        num=[]
        num.extend(answer2)
        a=int(num[0])-1
        b=int(num[1])-1
        c=int(num[2])-1
        score=pk(a,0)+pk(b,1)+pk(c,2)
    else:
        score=pk(0,0)+pk(1,1)+pk(2,2)
    if score>0:
        print('你最终获胜了，牛逼！')
    elif score<0:
        print('你最终输了，害！')
    else:
        print('平局，^_^')
main()




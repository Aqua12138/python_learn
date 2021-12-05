import random
import time
class Role():
    def __init__(self,name='【角色】'):
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)
class Knight(Role): 
    def __init__(self,name):
        Role.__init__(self,name)
        self.life=self.life*5
        self.attack=self.attack*3 
    def fight_buff(self,opponent):
        if opponent.name=='【暗影刺客】' :
            self.attack=self.attack*2  
class Assassin(Role):
    def __init__(self,name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life=self.life*3
        self.attack=self.attack*5
    def fight_buff(self,opponent):
        if opponent.name=='【精灵弩手】' :
            self.attack=self.attack*2                            
class Bowman(Role):
    def __init__(self,name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life=self.life*4
        self.attack=self.attack*4
    def fight_buff(self,opponent):
        if opponent.name=='【圣光骑士】' :
            self.attack=self.attack*2  
class game():
    def __init__(self):
        self.players = []
        self.enemies = []
        self.score = 0
        self.game_start()
        self.born_role()
        self.fight_buff2()
        self.show_role()
        self.order()
        for i in range(3):
            self.pk(i)
        self.pk_result()
    #角色配合
    def fight_buff2(self):
        if self.players[0].name==self.players[1].name and self.players[1].name==self.players[2].name:
            for i in range(3):
                self.players[i].life=self.players[i].life*1.25
        elif self.players[0].name!=self.players[1].name and self.players[1].name!=self.players[2].name and self.players[2].name!=self.players[0].name:
            for i in range(3):                    
                self.players[i].attack=self.players[i].attack*1.25
        else:
            pass
        if self.enemies[0].name==self.enemies[1].name and self.enemies[1].name==self.enemies[2].name:
            for i in range(3):
                self.enemies[i].life=self.enemies[i].life*1.25
        elif self.enemies[0].name!=self.enemies[1].name and self.enemies[1].name!=self.enemies[2].name and self.enemies[2].name!=self.enemies[0].name:
            for i in range(3):                    
                self.enemies[i].attack=self.enemies[i].attack*1.25
        else:
            pass
    #角色生成
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(name ='【圣光骑士】'),Assassin(),Bowman()]))#抽取一个类的实例对象
            self.enemies.append(random.choice([Knight(),Assassin(),Bowman()]))
        
    #展示角色
    def game_start(self):
        print('---------欢迎来到赛尔号--------')
        print('在昔日的赛尔飞艇上，有一个邪恶的大魔头，\n大魔头座下有3位精灵之王,三位精灵之王\n分别掌握着水火木三种属性。\n只有打败大魔王，赛尔飞艇才能重新运转，上吧！，我的赛尔勇士！')
        H=input('按回车以继续\n')
        if H=='\n':
            pass
    def show_role(self):
        print('-----------角色信息-----------')
        print('你的队伍：')
        for i in range(3):
            print('【我方】 {}血量：{} 攻击力：{}'.format(self.players[i].name,self.players[i].life,self.players[i].attack))
            time.sleep(1.5)
        print('------------------------------')
        print('敌方队伍：')
        for j in range(3):
            print('【敌方】 {}血量：{} 攻击力：{}'.format(self.enemies[j].name,self.enemies[j].life,self.enemies[j].attack))
            time.sleep(1.5)
        print('------------------------------')
        H=input('按回车以继续\n')
        if H=='\n':
            pass
    def pk(self,i):
        self.players[i].fight_buff(self.enemies[i])
        self.enemies[i].fight_buff(self.players[i])
        while self.players[i].life>0 and self.enemies[i].life>0:
            self.players[i].life= self.players[i].life-self.enemies[i].attack
            self.enemies[i].life=self.enemies[i].life-self.players[i].attack
            print('{}发起了攻击，【玩家】剩余血量：{}'.format(self.players[i].name,self.players[i].life))
            print('{}发起了攻击，【敌人】剩余血量：{}'.format(self.enemies[i].name,self.enemies[i].life))
            print('------------------------------')
            time.sleep(1.5)
        if self.players[i].life>0 and self.enemies[i].life<=0:
            print('你赢了！')
            self.score=self.score+1
        elif self.players[i].life<=0 and self.enemies[i].life>0:
            print('你输了。')
            self.score=self.score-1
        else:
            print('你们同归于尽了。')
        print('------------------------------')
        time.sleep(1.5)
        H=input('按回车以继续\n')
        if H=='\n':
            pass
    def order(self):
        player_order={}
        for i in range(3):
            while True:
                A=int(input('你想将{}放在第几个出场'.format(self.players[i].name)))
                if A  in [1,2,3]:
                    break
                else:
                    print('请输入1～3的数字')
            player_order[A]=self.players[i]
        self.player=[]
        for i in range(1,4):
            self.players.append(player_order[i])
        print('敌人队伍出场顺序：{} {} {}'.format(self.enemies[0].name,self.enemies[1].name,self.enemies[2].name))
        print('玩家队伍出场顺序：{} {} {}'.format(self.players[0].name,self.players[1].name,self.players[2].name))    
    def pk_result(self):
        if self.score>0:
            print('你拯救了世界')
        elif self.score<0:
            print('世界因你终结')
        else:
            print('人们会纪念你')
game1=game()
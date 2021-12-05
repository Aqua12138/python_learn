import pygame
import random
pygame.init()
#创建窗口大小常量
SCREEN_RECT=pygame.Rect(0,0,532,1319)
#设置帧数常数
FPS=60
#设置敌方出现事件
TIME=pygame.USEREVENT
TIME_2=pygame.USEREVENT+5
#英雄发射子弹事件
FIRE=pygame.USEREVENT+1
FIRE_enemy=pygame.USEREVENT+3
#设定子弹发射速度
#敌方游戏精灵
class GameSprite(pygame.sprite.Sprite):
    '''飞机大战游戏精灵'''
    def __init__(self,image_name,speed=1):
        #调用父类的继承方法
        super().__init__()
        self.image=pygame.image.load(image_name)#加速绘制
        self.rect=pygame.Rect(random.randint(0,532-64),0,64,64)
        self.speed=speed
    def update(self):
    #在屏幕的垂直方向移动
        self.rect.y+=self.speed
#背景游戏精灵
class background(GameSprite):
    def __init__(self,is_all=False):
        #调用父类的继承方法
        super().__init__('飞机大战/picture/背景_副本.png')
        self.rect=pygame.Rect(0,0,532,1319)#注意不能使用SCREEN_RECT，参数会发生改变，类将被改写
        if is_all==True:
            self.rect.y=-self.rect.height
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height
class enemy(GameSprite):
    def __init__(self):
        super().__init__('飞机大战/picture/敌人.png')
        self.speed=random.randint(1,3)
        self.bullents_enemy_1=pygame.sprite.Group()
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.kill()          
    def fire(self):#########
        #1.#创建子弹精灵
        bullet_enemy=Bullent_enemy()
        #2.设置位置
        bullet_enemy.rect.bottom=self.rect.bottom+70
        bullet_enemy.rect.centerx=self.rect.centerx+25
        #3.添加到精灵组
        self.bullents_enemy_1.add(bullet_enemy)
class enemy2(GameSprite):
    def __init__(self):
        super().__init__('飞机大战/picture/敌人2.png')
        self.speed=random.randint(5,8)
        self.bullents_enemy_2=pygame.sprite.Group()
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.kill()
    def fire(self):#########
        #1.#创建子弹精灵
        bullet_enemy=Bullent_enemy()
        #2.设置位置
        bullet_enemy.rect.bottom=self.rect.bottom+70
        bullet_enemy.rect.centerx=self.rect.centerx+25
        #3.添加到精灵组
        self.bullents_enemy_2.add(bullet_enemy)
class enemy3(GameSprite):
    def __init__(self):
        super().__init__('飞机大战/picture/敌人3.png')
        self.speed=random.randint(10,12)
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.kill()
class Hero(GameSprite):
    def __init__(self):
        super().__init__('飞机大战/picture/飞机.png',0)
        self.rect.centerx=SCREEN_RECT.centerx#模型中点
        self.rect.bottom=SCREEN_RECT.bottom-120#模型底部
        self.speed_1=0
        self.speed_2=0  
        #创建子弹精灵组
        self.bullents=pygame.sprite.Group()
    def update(self):
        self.rect.x+=self.speed_1
        self.rect.y+=self.speed_2
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>532:#模型右侧
            self.rect.right=532
        elif self.rect.y<0:
            self.rect.y=0
        elif self.rect.bottom>1319:
            self.rect.bottom=1319
    def fire(self):
        #1.#创建子弹精灵
        bullet=Bullent()
        #2.设置位置
        bullet.rect.bottom=self.rect.top-10
        bullet.rect.centerx=self.rect.centerx+24
        #3.添加到精灵组
        self.bullents.add(bullet)
class Bullent(GameSprite):
    def __init__(self):
        super().__init__('飞机大战/子弹.png',-10)
    def update(self):
        super().update()
        if self.rect.bottom<0:
            self.kill()
    def __del__(self):
        pass  
class  Bullent_enemy(GameSprite):#########
    def __init__(self):
        super().__init__('飞机大战/picture/敌人子弹3.png',8)
    def update(self):
        super().update()
        if self.rect.bottom>1319:
            self.kill()
    def __del__(self):
        pass  




# def aa():
#     pygame.init()
#     #初始化窗口
#     screen=pygame.display.set_mode((400,600))
#     #绘制图像背景
#     #1加载图像数据
#     background=pygame.image.load('飞机大战/AnimatedStreet.png')
#     #2绘制图像
#     screen.blit(background,(0,0))
#     #绘制英雄图像
#     #1
#     hero=pygame.image.load('飞机大战/Player.png')
#     #2
#     screen.blit(hero,(200,500))
#     #3更新显示
#     pygame.display.update()
#     #创建时钟对象
#     clock=pygame.time.Clock()
#     #1定义hero初始位置
#     hero_rect=pygame.Rect(200,500,44,96)
#     #创建敌人飞机位置
#     enemy_1=GameSprite('飞机大战/Enemy.png')
#     enemy_2=GameSprite('飞机大战/Enemy.png',2)
#     #创建敌机的精灵组
#     enemy_group=pygame.sprite.Group(enemy_1,enemy_2)
#     #循环开始意味着游戏开始
#     while True:
#         #1可以控制循环体的执行速度
#         clock.tick(60)#刷新帧数
#         #捕获用户的操作
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 print('游戏退出...')
#                 #卸载所有模块
#                 pygame.quit()
#                 #终止当前所有的程序
#                 exit()
#         #3修改飞机位置
#         if hero_rect.y<=-96:
#             hero_rect.y=600
#         else:
#             hero_rect.y-=1
#         #4修改飞机
#         screen.blit(background,(0,0))#覆盖之前的汽车位置，使得只有一个汽车出现
#         screen.blit(hero,hero_rect)


#         #精灵组调用两个方法
#         #更新实时位置
#         enemy_group.update()
#         #绘制
#         enemy_group.draw(screen)
#         pygame.display.update()
#     pygame.quit()







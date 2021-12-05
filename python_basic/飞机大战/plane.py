import pygame
import plane2
import random
class PlaneGame(object):
    def __init__(self):
        print('游戏初始化')
        #1.创建游戏窗口
        self.screen=pygame.display.set_mode(plane2.SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock=pygame.time.Clock()
        #3.调用私有精灵
        self.__create_sprites()
        #4.设置定时事件创建敌人
        pygame.time.set_timer(plane2.TIME,10000)
        pygame.time.set_timer(plane2.TIME_2,20000)
        #5.设定子弹发射
        pygame.time.set_timer(plane2.FIRE,500)
        pygame.time.set_timer(plane2.FIRE_enemy,1000)##########
        #定义分数
        self.score=0
    def start_game(self):
        print('游戏开始...')
        while True:
            #1.设置刷新频率
            self.clock.tick(plane2.FPS)
            #2.监听
            self.__event_handler()
            #3.碰撞检测
            self.__cleck_collide()
            #4.绘制
            self.__update_sprites()
            #5.更新位置
            pygame.display.update()
    def __create_sprites(self):
        #创建背景精灵和敌人精灵组
        bg1=plane2.background()
        bg2=plane2.background(True)
        self.back_group=pygame.sprite.Group(bg1,bg2)
        #创建敌人精灵组
        self.enemy=plane2.enemy()#########
        self.enemy2=plane2.enemy2()#########
        self.enemy3=plane2.enemy()
        self.enemy4=plane2.enemy3()
        self.enemy_group=pygame.sprite.Group()
        self.enemy_group2=pygame.sprite.Group()
        #创建英雄精灵
        self.hero=plane2.Hero()
        self.hero_group=pygame.sprite.Group(self.hero)
    def __event_handler(self):
        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type==pygame.QUIT:
                self.__game_over()
            if event.type==plane2.TIME:
                self.enemy=plane2.enemy()
                self.enemy3=plane2.enemy()
                self.enemy_group.add(self.enemy,self.enemy3)   
            elif event.type==plane2.TIME_2:
                self.enemy2=plane2.enemy2()
                self.enemy_group.add(self.enemy2)
            elif random.randint(1,50)==30:
                self.enemy4=plane2.enemy3()
                self.enemy_group2.add(self.enemy4)
            elif len(self .enemy_group)==0:
                self.enemy=plane2.enemy()
                self.enemy3=plane2.enemy()
                self.enemy_group.add(self.enemy,self.enemy3)            
            # elif event.type==plane2.TIME_2:
            if event.type==plane2.FIRE_enemy:
                for i in self.enemy_group:
                    i.fire()
            #第一种移动方式
            #elif event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                #print('右')
            #第二种移动方式，更加灵活，不用再重新点击
            keys_pressed=pygame.key.get_pressed()#获得键盘元组
            #手控发射子弹
            if event.type==plane2.FIRE:
                if keys_pressed[pygame.K_x]:
                    self.hero.fire()   
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed_1=6
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed_1=-6
            elif keys_pressed[pygame.K_UP]:
                self.hero.speed_2=-6
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.speed_2=6
            else:
                self.hero.speed_1=0
                self.hero.speed_2=0
    def __cleck_collide(self):
        aa=len(pygame.sprite.groupcollide(self.hero.bullents,self.enemy_group,True,True))+len(pygame.sprite.groupcollide(self.hero.bullents,self.enemy_group2,True,True))
        if aa==1:
            self.score+=1
        enemies=len(pygame.sprite.spritecollide(self.hero,self.enemy_group,True))+len(pygame.sprite.spritecollide(self.hero,self.enemy.bullents_enemy_1,True))+len(pygame.sprite.spritecollide(self.hero,self.enemy2.bullents_enemy_2,True))+len(pygame.sprite.spritecollide(self.hero,self.enemy_group2,True))
        if enemies>0:
            self.__game_over()
        
    #更新
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group2.update()
        self.enemy_group2.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullents.update()
        self.hero.bullents.draw(self.screen)
        self.enemy.bullents_enemy_1.update()
        self.enemy.bullents_enemy_1.draw(self.screen)
        self.enemy2.bullents_enemy_2.update()
        self.enemy2.bullents_enemy_2.draw(self.screen)
        self.enemy3.bullents_enemy_1.update()
        self.enemy3.bullents_enemy_1.draw(self.screen)
    def __game_over(self):
        print('游戏结束')
        print('score={}'.format(self.score))
        pygame.quit()
        exit()

if __name__=='__main__':
 #创建游戏对象
    pygame.init()
    game=PlaneGame()
    game.start_game()





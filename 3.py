import pygame,sys
from pygame.locals import *
import time
import random
#创建一个飞机类
class plane(object):
    def __init__(self):
        planeImage='hero.jpg'
        self.image=pygame.image.load(planeImage).convert()
        self.name='player'
        #设置飞机的默认坐标
        self.x=150
        self.y=600
        #飞机的子弹
        self.bullet=[]
    #将飞机画出了来
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
    #飞机的移动
    def keyOperation(self,keyValue):
        if keyValue=='left':
            print("--按下 左键--")
            self.x-=10
        elif keyValue=='right':
            print("--按下 右键--")
            self.x+=10
        elif keyValue=='space':
            print("按下 空格键")
            self.bullet.append(Bullet(self.name,self.x+35,self.y-32))

#子弹            
class Bullet(object):
    def __init__(self,name,x,y):
        self.x=x
        self.y=y
        self.name=name
        if self.name=='player':
            bgImage='bullet.jpg'
            self.b=pygame.image.load(bgImage).convert()
        elif self.name=='emery':
            bgImage='en.jpg'
            self.b=pygame.image.load(bgImage).convert()
    #画出子弹
    def draw(self,screen):
        if self.name=='player':
            self.y-=4
        elif self.name=='emery':
            self.y+=4
        screen.blit(self.b,(self.x,self.y))

#敌人的飞机
class emery(object):
    def __init__(self,x=10,y=10):
        self.x=x
        self.y=y
        bgImage='em.jpg'
        self.e=pygame.image.load(bgImage).convert()
        self.name='emery'
        self.bullet=[]
        self.direction='right'
    def draw(self,screen):
        screen.blit(self.e,(self.x,self.y))
    def move(self,screen):
        if self.direction=='right':
            self.x+=2
        elif self.direction=='left':
            self.x-=2
        if self.x>420:
            self.direction='left'
        elif self.x<20:
            self.direction='right'
        rand=random.randint(1,100)
        if rand in [1,7]:
            self.bullet.append(Bullet(self.name,self.x+5,self.y+30))
        for temp in self.bullet:
            temp.draw(screen)


        
#主程序
if __name__=='__main__':
    screen=pygame.display.set_mode((480,890),0,32)
    bgImage='background.jpg'
    background=pygame.image.load(bgImage).convert()
    #创建飞机
    player=plane()
    #创建敌机
    em=emery()
    while True:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                print("exit")
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    print('left')
                    player.keyOperation('left')
                elif event.key==K_d or event.key==K_RIGHT:
                    print('right')
                    player.keyOperation('right')
                elif event.key==K_SPACE:
                    print('space')
                    player.keyOperation('space')
        player.draw(screen)
        em.draw(screen)
        em.move(screen)
        #if player.bullet!='':
            #player.bullet.draw(screen)
        for temp in player.bullet:
            temp.draw(screen)
        pygame.display.update()
        time.sleep(0.01)

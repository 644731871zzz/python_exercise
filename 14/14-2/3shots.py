import pygame
import sys

from pygame.sprite import Sprite

from ship import Ship
from settings import Settings
from bullet import Bullet
from rectangle import Rectangle
from button import Button
from game_stats import Stats

class Shots:
    def __init__(self):
        """初始化游戏"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        #配置屏幕
        self.screen=pygame.display.set_mode((self.settings.screen_width,
                                        self.settings.screen_height))
        pygame.display.set_caption("3shots")
        self.screen_rect=self.screen.get_rect()

        #调用ship类,要放在后面,因为前面初始函数有ship类需要的信息
        self.ship=Ship(self)

        #创建bullets精灵类
        self.bullets=pygame.sprite.Group()

        #调用矩形类
        self.rectangle=Rectangle(self)

        #调用按钮类
        self.button=Button(self,"Play")

        #调用记分类
        self.stats=Stats(self)

        #游戏开始状态
        self.game_active=False


    def rungame(self):
        """开始游戏"""

        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self.rectangle.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """捕捉玩家的输入"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_mousedown_event(mouse_pos)
    
    def _check_keydown_event(self,event):
        """相应键盘按下的事件"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self,event):
        """键盘抬起的事件"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False
    
    def _check_mousedown_event(self,mouse_pos):
        """相应鼠标按下"""
        #检测是否在坐标内
        button_chicked=self.button.rect.collidepoint(mouse_pos)
        if button_chicked and not self.game_active:
            #重置游戏开始运行速度
            self.settings.inirialize_dynamic_settings()
            self._start_game()

    def _start_game(self):
        """点击按钮开始游戏"""
        #重置游戏系统信息
        self.bullets.empty()
        #重置飞船位置
        self.ship.place_ship()
        #重置备弹信息
        self.stats.reset_stats()

        self.game_active=True

        #隐藏光标
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """子弹的发射事件"""
        if self.stats.bullet_left>0:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.bullet_left-=1

    def _update_bullet(self):
        """更新子弹"""
        #更新子弹的位置,删除在屏幕边缘外的子弹,每一次击中将会增加游戏整体运行速度
        for bullet in self.bullets.sprites():
            bullet.update()
            if pygame.sprite.spritecollideany(self.rectangle
                                              ,self.bullets)==bullet:
                self.bullets.remove(bullet)
                self.stats.bullet_left+=1
                self.settings.increase_speed()
            elif bullet.rect.left>self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        
        #如果3颗子弹没有击中,游戏都结束
        if self.stats.bullet_left==0 and len(self.bullets)==0:
            self.game_active=False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """更新屏幕图像"""
        #将屏幕底色进行绘制
        self.screen.fill(self.settings.screen_color)

        #绘制飞船
        self.ship.blitme()

        #绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #绘制矩形
        self.rectangle.draw_rect()

        if not self.game_active:
            self.button.draw_button()

        pygame.display.flip()

if __name__=="__main__":
    ai=Shots()
    ai.rungame()


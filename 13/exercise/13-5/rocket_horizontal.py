import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GamesStats
from bullet import Bullet
from ship import Ship
from alien import Alien

class Rocket_horizontal:
    """管理游戏资源和类的行为"""
    def __init__(self):
        """初始化游戏的资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        #屏幕设置
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        #创建窗口名称
        pygame.display.set_caption("rocket horizontal")

        self.stats=GamesStats(self)

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        self._create_fleet()

        self.game_active=True

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()

            if self.game_active==True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        """相应按键鼠标事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """相应按下"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """相应释放"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        if event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def _fire_bullet(self):
        """创建子弹并加入编组"""
        if len(self.bullets)<self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的纸质并删除已经消失的子弹"""
        #更新子弹的位置
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left >=1200:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):

        #检查是否有子弹击中了外星人,如果是,删除对应子弹和外星人
        collisions=pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True
        )
        if not self.aliens:
            #删除现有子弹并添加新的外星舰队
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        #检查外星人与飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        #检查是否有外星人到达屏幕的下边缘
        self._check_aliens_bottom()

    def _create_fleet(self):
        """创建外星人舰队"""
        #创建一个外星人舰队,不断添加,直到没有空间添加外星人为止
        #外星人的间距间距为外星人的宽度
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size

        current_x=self.settings.screen_width-2*alien_width
        current_y=alien_height
        while current_x>3*alien_width:
            while current_y<(self.settings.screen_height-3*alien_height):
                self._create_alien(current_x,current_y)
                current_y+=2*alien_height
            
            #添加第一列外星人后重置y并递减x
            current_y=alien_height
            current_x-=2*alien_width

    def _create_alien(self,x,y):
        """创建一个外星人并放置"""
        new_alien=Alien(self)
        new_alien.x=x
        new_alien.rect.x=x
        new_alien.rect.y=y
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """将整个外星人舰队向左移动,并改变上下方向"""
        for alien in self.aliens.sprites():
            alien.rect.x-=self.settings.fleet_move_left
        self.settings.fleet_direction*=-1

    def _ship_hit(self):
        """响应飞船和外星人碰撞"""
        if self.stats.ships_left>0:
            #将ship_left-=1
            self.stats.ships_left-=1

            #清空外星人和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            #创建一个新的外星人舰队,将飞船放在屏幕底部
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active=False

    def _check_aliens_bottom(self):
        """检查是否有外星人触及屏幕右侧边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.left<=0:
                #像飞船被撞到一样处理
                self._ship_hit()
                break

    def _update_screen(self):
        """更新屏幕上的图像"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #将画面显示到屏幕
        pygame.display.flip()

if __name__=='__main__':
    #创建游戏实例并运行
    ai=Rocket_horizontal()
    ai.run_game()
                    
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        """创建子弹的信息"""
        super().__init__()
        #引入ai_game信息
        self.ship=ai_game.ship
        self.settings=ai_game.settings
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #配置子弹尺寸与颜色,创建后再配置子弹的正确位置
        self.bullet_color=self.settings.bullet_color
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,
                                     self.settings.bullet_height)
        self.rect.midright=ai_game.ship.image_rect.midright

        #使用浮点存储子弹移动坐标
        self.x=float(self.rect.x)

    def update(self):
        """更新子弹的位置信息"""
        self.x+=self.settings.bullet_speed
        self.rect.x=self.x

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)

import pygame

class Ship:
    """创建一个飞船的类"""
    def __init__(self,ai_game):
        """初始化所需信息"""
        #获取屏幕信息
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        #加载飞船图像
        self.image=pygame.image.load('image/ship.bmp')
        self.image_rect=self.image.get_rect()
        #将飞船绘制在左侧边缘中央
        self.image_rect.midleft=self.screen_rect.midleft
        self.y=float(self.image_rect.y)
        
        #移动标志
        self.moving_up=False
        self.moving_down=False

    def place_ship(self):
        """重新放置飞船"""
        self.image_rect.midleft=self.screen_rect.midleft
        self.y=float(self.image_rect.y)
        
        
    def update(self):
        """控制飞船的移动"""
        #向上
        if self.moving_up and self.image_rect.top>=0:
            self.y-=self.settings.ship_speed
        #向下
        if (self.moving_down and 
            self.image_rect.bottom<=self.settings.screen_height):
            self.y+=self.settings.ship_speed

        #更新y的值
        self.image_rect.y=self.y

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image,self.image_rect)
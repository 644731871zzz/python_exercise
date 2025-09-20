import pygame

class Rectangle:
    def __init__(self,ai_game):
        """创建矩形基本信息"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings

        self.rect=pygame.Rect(0,0,self.settings.rect_width,
                              self.settings.rect_height)
        
        self.rect.midright=self.screen_rect.midright
        
        self.top=float(self.rect.top)
        self.bottom=float(self.rect.bottom)
        
        #矩形移动方向,1为向下
        self.move_direction=1

    def update(self):
        """更新矩形位置"""
        #向下移动
        if self.move_direction==1:
            self.rect.y+=self.move_direction*self.settings.rect_speed
        #向上移动
        elif self.move_direction==-1:
            self.rect.y+=self.move_direction*self.settings.rect_speed
        #在触碰边缘时候改变方向
        if self.rect.bottom>=self.screen_rect.bottom or self.rect.top<=0:
            self.move_direction*=-1

    def draw_rect(self):
        """绘制矩形"""
        pygame.draw.rect(self.screen,self.settings.rect_color,self.rect)
import pygame

class Settings:
    """创建settings类"""
    def __init__(self):
        #设置屏幕参数
        self.screen_width=1200
        self.screen_height=800
        self.screen_color=(120,120,120)

        #设置子弹参数
        self.bullet_width,self.bullet_height=20,5
        self.bullet_color=(0,0,255)
        self.bullet_limit=3

        #设置矩形参数
        self.rect_width=100
        self.rect_height=400
        self.rect_color=(0,0,255)

        #设置按钮参数
        self.button_width=200
        self.button_height=50
        self.button_color=(0,135,0)

        #提高速度的倍数
        self.speedup_scale=1.1

        self.inirialize_dynamic_settings()

    def inirialize_dynamic_settings(self):
        """初始化可变化的速度数值"""
        self.ship_speed=3.0
        self.bullet_speed=10
        self.rect_speed=3.0

    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.rect_speed*=self.speedup_scale
        

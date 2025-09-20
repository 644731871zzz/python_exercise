import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """创建新的外星人组"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen

        self.image=pygame.image.load('image/alien.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.settings.screen_width-self.rect.width
        self.rect.y=self.rect.height

        x,y=self.rect.size
        self.x,self.y=x,y

    def check_edges(self):
        """如果外星人在边缘,返回True"""       
        screen_rect=self.screen.get_rect()
        return(self.rect.bottom>=screen_rect.bottom)or (self.rect.top<=0)
    
    def update(self):
        self.y+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.y=self.y

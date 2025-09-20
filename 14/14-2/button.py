import pygame

class Button:
    """创建按钮类"""
    def __init__(self,ai_game,msg):
        """创建初始属性"""
        #获取屏幕属性
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #配置按钮大小
        self.width=ai_game.settings.button_width
        self.height=ai_game.settings.button_height
        self.button_color=ai_game.settings.button_color

        #配置文字参数
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #创建对象,并居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #显示按钮
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """将msg渲染为图像,使其在按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,
                                        self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        """绘制填充按钮再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
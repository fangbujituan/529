'''
选择用于表示飞船的图像后，需要将其显示到屏幕上。我们将创建一个名为ship的模块，其
中包含Ship类，它负责管理飞船的大部分行为。

时间：2019.7.2
'''
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置其初始位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')   # 为加载图像,这个函数返回一个表示飞船的surface
        self.rect = self.image.get_rect()  # 加载图像后，我们使用get_rect()获取相应surface的属性rect
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # 移动标志                         飞船不动时，标志moving_right将为False。玩家按下右箭头键时，我们将这个标志设置为True；而玩家松开时，我们将这个标志重新设置为False。
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动位置调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

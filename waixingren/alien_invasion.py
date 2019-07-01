"""
说明文档：
开发过程：
    1、编码前，安装Pygame
    2、创建 Pygame 窗口以及响应用户输入
    3、设置背景色
    4、创建设置类
  * 5、添加飞船图像

"""
# 首先，我们创建一个空的Pygame窗口。使用Pygame编写的游戏的基本结构如下
import sys
import pygame
from settings import Settings


# 创建空的py窗口
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))    # 创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 退出程序，抛出异常
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
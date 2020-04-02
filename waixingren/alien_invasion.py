"""
说明文档：

时间：2019.7.1

"""
# 首先，我们创建一个空的Pygame窗口。使用Pygame编写的游戏的基本结构如下
import sys
import pygame
from waixingren.settings import Settings
from waixingren.ship import Ship
from waixingren.alien import Alien
import waixingren.game_functions as gf
from pygame.sprite import Group
from waixingren.game_stats import GameStats
from waixingren.button import Button
from waixingren.scoreboard import Scoreboard





# 创建空的py窗口
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))    # 创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)

    # 开始游戏的主循环q
    while True:

        # 将事件循环（重构屏幕）换为对函数check_events()的调用
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 每次执行循环时都调用飞船的方法update()
            ship.update()

            # 对子弹的操作
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # 更新外星人的位置
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 更新屏幕的代码替换为对函数update_screen()的调用
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


        # # 监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         # 退出程序，抛出异常
        #         sys.exit()


run_game()
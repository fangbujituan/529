'''
每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为settings的模块，
其中包含一个名为Settings的类，用于将所有设置存储在一个地方，以免在代码中到处添加设置。
这样，我们就能传递一个设置对象，而不是众多不同的设置。另外，这让函数调用更简单，且在
项目增大时修改游戏的外观更容易：要修改游戏，只需修改settings.py中的一些值，而无需查找
散布在文件中的不同设置。
'''
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):

        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)# 背景颜色为白色
        # self.bg_color = (70, 149, 222)# 背景颜色为蓝色

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 1    # 子弹速度，默认3
        self.bullet_width = 3   # 子弹宽度，默认3
        self.bullet_height = 15    # 子弹高度，默认15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # 外星人设置
        # self.alien_speed_factor = 1 # 外星人移动速度，默认1
        self.fleet_drop_speed = 10 # 外星人向下移动速度，默认10
        # self.fleet_direction = 1    # fleet_direction为1表示向右移，为-1表示向左
        # 随着等级提高，游戏进行的速度也在提高
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5 # 飞船移动速度 默认1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1 # 外星人移动的速度 默认为1

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
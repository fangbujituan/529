"""
计分：
    现在需要确定外星人与飞船发生碰撞时，该做些什么。我们不销毁ship实例并创建一个新的
    ship实例，而是通过跟踪游戏的统计信息来记录飞船被撞了多少次（跟踪统计信息还有助于记
分）。"""
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化游戏统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left  = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


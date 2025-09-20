class Stats:
    """跟踪游戏信息"""
    def __init__(self,ai_game):
        """初始化信息"""
        self.settings=ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """重置游戏关键信息"""
        self.bullet_left=self.settings.bullet_limit
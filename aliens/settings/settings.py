class Settings:
    """Class for keep all settings for game """

    def __init__(self):
        """Initialization settings in game, statics parameters """
        # 1)Param screen
        # широта
        self.screen_width = 980
        #  высота
        self.screen_height = 800
        self.bg_color = (250, 250, 250)
        self.FPS = 240
        # 2)Пули
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30
        # third)Aliens
        # fleet_direction = 1 обозновачет движение вправо, а -1 влево
        # 4) Ship
        self.ship_limit = 3
        self.fleet_drop_speed = 10

        # Temp of game
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходие игры."""
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 3
        self.aliens_speed = 5
        # 1 right -1 left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.aliens_speed *= self.speedup_scale
        self.alien_points *= self.speedup_scale

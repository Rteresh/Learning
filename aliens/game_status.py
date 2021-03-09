class GameStatus:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_status()
        #     Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False

        self.record = self.file_records()
        self.high_score = int(self.record)

    def reset_status(self):
        """Инициализирует статистику, изменяющихся в ходе игры """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    @staticmethod
    def file_records():
        try:
            with open('record') as record_file:
                record = record_file.read()
        except FileNotFoundError:
            with open('record', 'w') as record_file:
                record_file.write('1')
                record_file.close()
            with open('record', 'r') as record_file:
                record = record_file.read()
        return record

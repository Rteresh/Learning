import sys
import pygame
from setting.settings import Settings
from mine_objects.combine import Combine


class Mine:
    """Класс для управления ресурсами и поведения игры """

    def __init__(self):
        """Инициализирует игру и создаент игровые ресурсы"""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption(self.setting.screen_name)
        self.combine = Combine(self.screen)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self.screen.fill(self.setting.bg_color)
            self.combine.blitme()
            # Отслеживание событий  на экране,клавиатуры и мыши
            pygame.display.flip()


if __name__ == '__main__':
    mine = Mine()
    mine.run_game()

import pygame


class Combine:
    """Класс для управления комбайном"""

    def __init__(self, mine_screen):
        """Инициализация коробля и начальной позиции"""
        self.screen = mine_screen
        self.screen_rect = mine_screen.get_rect()

        #      Zagruzka photo combine

        self.image = pygame.image.load('templates/combine.jpg')
        self.rect = self.image.get_rect()
        # Evry new combine set bottom
        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        """Рисует комбайн"""
        self.screen.blit(self.image, self.rect)

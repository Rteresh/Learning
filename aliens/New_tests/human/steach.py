import pygame


class Stiech:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('New_tests/images/stiech.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centrx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

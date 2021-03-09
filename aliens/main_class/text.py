import pygame
from time import sleep


class WinText:
    def __init__(self, ai_settings, screen, msg):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_colot = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.text_image = self.font.render(msg, True, self.text_colot, self.ai_settings.bg_color)
        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.centerx = self.screen_rect.centerx
        self.text_image_rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.text_image, self.text_image_rect)


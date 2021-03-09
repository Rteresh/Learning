import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """Initialization  main_class and set him position """
        super(Ship, self).__init__()
        self.moving_down = False
        self.moving_up = False
        self.screen = screen
        self.ai_settings = ai_settings

        # load ships image and take rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # every a new main_class will appear in bottom screen
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        # Две координаты
        self.centery = float(self.rect.centery)
        # левая позиция
        # self.centerx = float(ai_settings.ship_start_position_left+self.image.get_rect().centery)
        # правая позиция
        self.centerx = float(self.screen_rect.right - self.image.get_rect().centerx)

        # Каждый новый корабль появляется у нижнего края экрана

    def update(self):
        """UPDATE position main_class about with flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw a main_class in position"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self, ai_settings):
        """Размещает корабль в центре нижней стороры."""
        self.centerx = self.screen_rect.centerx
        self.centery = ai_settings.screen_height - self.image.get_height() / 2

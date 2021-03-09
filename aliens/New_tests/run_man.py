import pygame

from New_tests.settings.settings import Settings
from New_tests.human.steach import Stiech
import New_tests.settings.game_function as gf


def run():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    man = Stiech(screen)
    
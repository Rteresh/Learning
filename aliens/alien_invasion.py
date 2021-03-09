import pygame

from settings.settings import Settings
from main_class.ship import Ship
from pygame.sprite import Group
import settings.game_functions as gf
from game_status import GameStatus
from botton.botton import Button
from scoreboard import Scoreboard
from main_class.text import WinText


def run_game():
    """Здесь происходит, что обновляется на экране"""
    # initialization game and create object screen
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    # Создание группы пуль
    bull = Group()
    play_button = Button(ai_settings, screen, "LET'S GO")
    play_button2 = WinText(ai_settings,screen,'TERESH WIN SHPAK LOX')
    aliens = Group()
    status = GameStatus(ai_settings)
    score = Scoreboard(ai_settings, screen, status)
    gf.create_fleet(ai_settings, screen, aliens, ship)
    time = pygame.time.Clock()
    # Run main loops game
    # Запуск основного цикла
    while True:
        gf.check_events(ship, ai_settings, bull, screen, status, play_button, aliens, score)
        if status.game_active:
            # Check Events mouse & board
            ship.update()
            gf.update_bullets(bull, aliens, ai_settings, screen, ship, status, score,play_button2)
            gf.update_aliens(aliens, ai_settings, ship, status, screen, bull, score)
            time.tick(ai_settings.FPS)
        gf.update_screen(ai_settings, screen, ship, bull, aliens, status, play_button, score,play_button2)

    # Show last changed screen


run_game()

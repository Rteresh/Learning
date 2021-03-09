import pygame


class Button:
    def __init__(self, ai_settings, screen, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение рамзеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (192, 192, 192)
        self.text_color = (255, 255, 255)
        # Ноне это шрифт по умолчанию, а 48 это размер шрифта
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивая по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        # Берет текст и пуф в картинку, второй аргумент это сглаживане
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отоброжение пустой кнопки и вывод сообщения"""
        # Рисует прямоугольную часть кнопки и вывод сообщения.
        self.screen.fill(self.button_color, self.rect)
        # Выводит изображение текста на экран с передачей изображения и обьекта rect
        self.screen.blit(self.msg_image, self.msg_image_rect)


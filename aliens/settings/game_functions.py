import sys
import pygame
from main_class.bullet import Bullet
from main_class.alien import Alien
from time import sleep


def check_events(ship, ai_settings, bullet, screen, stats, play_button, aliens, sb):
    """Обновление событий, которые проходят в основном классе """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys_exit(stats)
        elif event.type == pygame.KEYDOWN:
            moving_ship_keydown(ship, event, screen, bullet, ai_settings, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            moving_ship_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, bullet, aliens, ship, ai_settings, screen, sb)


def update_bullets(bull, aliens, ai_settings, screen, ship, stats, score,tx):
    bull.update()
    # копируем массив пуль и если пуля доходит до 0(положение/точнее до конца края экрана), то ее удаляют
    for bullet in bull.copy():
        if bullet.rect.bottom <= 0:
            bull.remove(bullet)
    # При обноружении попадания пули в пришельца, удаляется пуля и пришелец
    check_bullet_alien_collisions(bull, aliens, ai_settings, screen, ship, stats, score,tx)


def update_screen(ai_settings, screen, ship, bullets, alien, stats, play_button, score,tx):
    """ Обновляет изображение на экране и отображает новый экрv ан"""
    # При каждом новом проходе цикла  перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    # blitme() это функция для рисования пришельцев и коробля
    ship.blitme()
    alien.draw(screen)
    if len(alien) == 0:
        tx.blitme()
    # Вывод на экран счет
    score.show_score()
    # Кнока Play отображается в том случве, если игра неактивна
    if not stats.game_active:
        play_button.draw_button()


    # обновления экрана
    pygame.display.flip()


def moving_ship_keydown(ship, event, screen, bullet, ai_settings, stats, aliens, sb):
    """Что будет если нажать или удерживать кнопку"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        make_new_bullet(ai_settings, ship, bullet, screen, stats)
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_p:
        start_new_game(stats, aliens, bullet, ai_settings, screen, ship, sb)
    elif event.key == pygame.K_q:
        sys_exit(stats)


#             Дабы когда ты стреляешь и двигаешься вверх по диоганали, и чтобы пули
# стреляли из центра коробля необходимо в update коробля менять центр пули


def moving_ship_keyup(event, ship):
    """Что будет если отпустить кнопку """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def make_new_bullet(ai_settings, ship, bullets, screen, stats):
    """Функция для создания новых пуль"""
    if len(bullets) < ai_settings.bullet_allowed and stats.game_active:
        new_bullet = Bullet(ai_settings, ship, screen)
        bullets.add(new_bullet)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает в ряду"""
    # Создание пришельцев и вычисбение количества пришельцев в ряду.
    # Интервал между соседними пришельцами равен одной шиерне пришельца.
    # Create a first ryad aliens.
    alien = Alien(ai_settings, screen)
    # создается новое положение для пришельца(пришелец - ширина пришельца - пришелец)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = alien.y
    alien.rect.x = alien.x
    # Меняется расположение для следующих пришельцев
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """Создает флот пришельцев"""
    # Создание пришельца и вычисление количества пришельцев в ряду
    # Создается обЪект нового пришельца
    alien = Alien(ai_settings, screen)
    # количество пришельцев, которых можно создать в ряду
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_number = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

    # В этом цикле создается по одному новому пришельцу
    for row_numbers in range(row_number):
        for number_alien in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, number_alien, row_numbers)


def get_number_aliens_x(ai_settings, alien_width):
    """Создает пришельца и размещает его в ряду """
    # Здесь формула подсчета для пришельцев, сколько можно создать в ряду
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    """Определяет количество рядов, помещающихся на экране"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(aliens, ai_settings, ship, stats, screen, bullets, sb):
    """ Обновление пришельцев на экрана"""
    # Проверка границ
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, ship, bullets, sb)
    check_aliens_bottom(aliens, screen, ai_settings, stats, ship, bullets, sb)


def check_aliens_bottom(alien, screen, ai_settings, stats, ship, bullets, sb):
    screen_rect = screen.get_rect()
    for aliens in alien.sprites():
        if aliens.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, ship, bullets, sb)
            break


def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижения края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            # Меняет направление движение пришельцев
            for alien_sprites in aliens.sprites():
                alien_sprites.rect.y += ai_settings.fleet_drop_speed
            ai_settings.fleet_direction *= -1
            break


def check_bullet_alien_collisions(bullets, alien, ai_settings, screen, ship, stats, score,tx):
    collisions = pygame.sprite.groupcollide(bullets, alien, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        score.prep_score()
        check_high_score(stats, score)
    if len(alien) == 0:
        tx.blitme()




def ship_hit(ai_settings, stats, ship, bullets, sb):
    """Обрабытывает столкновение корабля с пришельцем."""

    if stats.ship_left == 1:
        # Обнуляет данные
        stats.reset_status()
        # Игра неактивна
        stats.game_active = False
        # Мышка видно
        pygame.mouse.set_visible(True)
    else:
        # Ументшение ship_left(settings)
        stats.ship_left -= 1
        # Обновление кол-во жизней
        sb.prep_ship()
        # Очистка списков пришельцев и пуль.
        bullets.empty()
    # Создание нового флота и размещение корабля в центре.
    ship.center_ship(ai_settings)


def delete_all_ojbects(aliens, bullets):
    aliens.empty()
    bullets.empty()


def check_play_button(stats, play_button, mouse_x, mouse_y, bullets, aliens, ship, ai_settings, screen, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        """Запускает новую игру при нажатии кнопки Play"""
        # Сброс игровой статистики
        start_new_game(stats, aliens, bullets, ai_settings, screen, ship, sb)


def start_new_game(stats, aliens, bullets, ai_settings, screen, ship, sb):
    stats.game_active = True
    stats.reset_status()
    sb.prep_level()
    # Указатель мыши скриывается
    pygame.mouse.set_visible(True)

    # очистка списков пришельцев и пуль
    delete_all_ojbects(aliens, bullets)

    create_fleet(ai_settings, screen, aliens, ship)
    ai_settings.initialize_dynamic_settings()

    # Обновление scoreboard изображений
    sb.prep_score()
    sb.prep_ship()


def check_high_score(stats, scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()


def sys_exit(stats):
    with open('record', 'w') as file_record:
        file_record.write(str(round(stats.high_score)))
    sys.exit()

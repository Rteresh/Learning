from random import choice


class RandomWalk:
    """Класс для генерирования случайных блуждений"""

    def __init__(self, num_points=5000):
        """Инициализир"""
        self.num_points = num_points

        # Все блуждания начниаются с точки (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""
        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # Отклоенение нулевых значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            print(self.y_values[-1])

            self.x_values.append(x)
            self.y_values.append(y)

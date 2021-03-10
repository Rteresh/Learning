from random import randint


class Die:
    def __init__(self, num_side=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_side = num_side

    def roll(self):
        """Возвращает случайное число от 1 до 6"""
        return randint(1, self.num_side)


dies = Die()
print(dies.num_side)

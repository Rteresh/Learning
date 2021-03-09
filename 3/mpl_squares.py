import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # Тут второй аргумент это толщина линни
# Назначение заголовка диаграммы и меток осей.
plt.title('Square Numbers', fontsize=24)  # Это у нас заголовок
plt.xlabel('Value', fontsize=14)  # Это у нас название координат х
plt.ylabel('Square of Value', fontsize=14)  # Это у нас название у координат
#  Назначение размера грифта делений на осях.
plt.tick_params(axis='both', labelsize=14)  # Это школа деления
plt.show()
print('test git')
import matplotlib.pyplot as plt

x_values = list(range(1, 1100))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.get_cmap('Greys'), edgecolors='none',
            s=40)  # s eto razmer tochki
plt.title('Square Numbers', fontsize=24)  # Это у нас заголовок
plt.xlabel('Value', fontsize=14)  # Это у нас название координат х
plt.ylabel('Square of Value', fontsize=14)  # Это у нас название у координат
#  Назначение размера грифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)  # Это школа деления
plt.axis([0, 1100, 0, 1000000])
plt.show()

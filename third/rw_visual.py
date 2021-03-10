import matplotlib.pyplot as plt
from third.random_walk import RandomWalk

while True:
    # Построение случайного блуждания.
    rw = RandomWalk(500000)
    rw.fill_walk()

    # Нанесите точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(40, 20), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.get_cmap('Blues'),
               edgecolors='none', s=5)
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('enter n')
    if keep_running == 'n':
        break

import matplotlib.pyplot as plt
from third.random_walk import RandomWalk

# Построение случайного блуждания.
rw = RandomWalk()
rw.fill_walk()

# Нанесите точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

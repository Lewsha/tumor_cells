"""Фазовый портрет с шумом"""

# Импортируем один из пакетов Matplotlib
import pylab
import main_functions


x_lists = []
y_lists = []

array = [[0.5, 500], [0.05, 500], [2, 200], [2.5, 100], [0.1, 200], [0.6, 300], [0.6, 0.1], [1.5, 100]]
for point_number in range(len(array)):
    print(point_number)
    result = main_functions.runge_cutt_noise(array[point_number])
    x_lists.append(result[0])
    y_lists.append(result[1])

# Нарисуем одномерный график
pylab.plot(x_lists[0], y_lists[0], x_lists[1], y_lists[1], x_lists[2], y_lists[2],
           x_lists[3], y_lists[3], x_lists[4], y_lists[4], x_lists[5], y_lists[5],
           x_lists[6], y_lists[6], x_lists[7], y_lists[7])

# Покажем окно с нарисованным графиком
pylab.show()

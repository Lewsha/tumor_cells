"""Фазовый портрет без шума"""

# Импортируем один из пакетов Matplotlib
import pylab
import main_functions


x_lists = []
y_lists = []

array = [[0.5, 0.05], [0.05, 100], [2.5, 500], [3.5, 300], [0.1, 200]]
for point_number in range(len(array)):
    print(point_number)
    result = main_functions.runge_cutt(array[point_number], mu=0.0026)
    x_lists.append(result[0])
    y_lists.append(result[1])

# Нарисуем одномерный график
pylab.plot(x_lists[0], y_lists[0], x_lists[1], y_lists[1], x_lists[2], y_lists[2],
           x_lists[3], y_lists[3])
pylab.tick_params(axis='both', which='major', labelsize=20)
pylab.yscale('log')
# Покажем окно с нарисованным графиком
pylab.show()

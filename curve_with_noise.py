"""Кривая с шумом (переходы между бассейнами притяжения)"""
# Импортируем один из пакетов Matplotlib
import pylab
import main_functions


x_lists = []
y_lists = []

array = [[0.18, 440]]
for point_number in range(len(array)):
    print(point_number)
    result = main_functions.runge_cutt_noise(array[point_number], epsilon=0.0009,
                                             mu=0.000264, h=0.01, points_count=100000)
    x_lists.append(result[0])
    y_lists.append(result[1])

# Нарисуем одномерный график
pylab.plot(x_lists[0], y_lists[0])

# Покажем окно с нарисованным графиком
pylab.show()

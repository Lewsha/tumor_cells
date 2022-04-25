"""Сетка кривых с шумом"""

# Импортируем библиотеку Math
import math
# Импортируем один из пакетов Matplotlib
import pylab
# Импортируем пакет со вспомогательными функциями
from matplotlib import mlab
import random


sigma = 0.1181
row = 1.131
eta = 20.19
delta = 0.3743
alfa = 1.636
beta = 0.002
mu = 0.003

epsilon = 0.3


def f(x, y):
    return sigma + (row * x * y)/(eta + y) - mu * x * y - delta * x + epsilon * random.gauss(0, 1)


def g(x, y):
    return alfa * y * (1 - beta * y) - x * y


h = 0.01
x_lists = []
y_lists = []


new_x = 0.05
new_y = 1
grid = [(new_x, new_y)]

for i in range(20):
    new_x = 0
    for j in range(35):
        grid.append([new_x, new_y])
        new_x += 0.1
    new_y += 25


array = [*grid]
for point_number in range(len(array)):
    print(point_number)
    x_list = [array[point_number][0]]
    y_list = [array[point_number][1]]
    for i in range(1, 10000):
        k1 = h * f(x_list[i - 1], y_list[i - 1])
        l1 = h * g(x_list[i - 1], y_list[i - 1])
        # print(f(x_list[i - 1], y_list[i - 1]), '\t', g(x_list[i - 1], y_list[i - 1]))
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0))
        l2 = h * g(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0))
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0))
        l3 = h * g(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0))
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3)
        l4 = h * g(x_list[i - 1] + k3, y_list[i - 1] + l3)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)
    x_lists.append(x_list)
    y_lists.append(y_list)

#print(x_list, '\n' * 5)
#print(y_list)

result = []
for x, y in zip(x_lists, y_lists):
    result.append(x)
    result.append(y)


# Нарисуем двумерный график
pylab.plot(*result)

# Покажем окно с нарисованным графиком
pylab.show()

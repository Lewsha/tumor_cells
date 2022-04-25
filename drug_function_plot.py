"""Графики функции 4 степени (с лекарствами) при разных значениях b"""

import math
import pylab
import matplotlib.ticker as ticker
from main_functions import *

b_list = [0.1*x for x in range(100)]
x_lists = []
y_lists = []
for i in range(len(b_list)):
    print(i)
    b = b_list[i]
    x = -10
    x_list = []
    y_list = []

    for j in range(100000):
        A = alfa * beta * mu
        B = -alfa * beta * row - alfa * mu + alfa * beta * mu + alfa * beta * mu * eta + alfa * beta * delta
        C = sigma + alfa * row - alfa * beta * row - alfa * mu - alfa * mu * eta + \
            alfa * beta * mu * eta + b * mu - alfa * delta + alfa * beta * delta + alfa * beta * delta * eta
        D = sigma * eta + sigma - b * row + alfa * row - alfa * mu * eta + b * mu * eta - \
            alfa * delta - alfa * delta * eta + alfa * beta * delta * eta + b * delta
        E = sigma * eta - alfa * delta * eta + b * delta * eta
        y = A*(x**4) + B*(x**3) + C*(x**2) + D*x + E

        x_list.append(x)
        y_list.append(y)

        x += 0.005

    x_lists.append(x_list)
    y_lists.append(y_list)
    pylab.plot(x_list, y_list, label=f'b = {b}')

pylab.grid(which='major',
           color='k',
           linewidth=1)
pylab.ylim(-50, 50)
pylab.show()


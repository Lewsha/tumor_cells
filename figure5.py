"""Построение figure 5 для отчета"""
import pylab
from main_functions import *
from separatrix import separatrix
from resting_points_calculation import resting_points_calc


def figure_5():
    """
    y_lists = []

    result = runge_cutt_noise((0.29054078392006955, 411.20391689484427), mu=0.0027, epsilon=0.0002, points_count=20000)
    pylab.plot(*result, zorder=2)
    y_lists.append(result[1])

    result = runge_cutt_noise((0.29054078392006955, 411.20391689484427), mu=0.0027, epsilon=0.0005, points_count=20000)
    pylab.plot(*result, zorder=1)
    y_lists.append(result[1])

    result = separatrix(mu=0.0027)
    pylab.plot(*result, zorder=1, color='red', linewidth=2, linestyle='dashed')
    pylab.scatter(0.5208856335983751, 340.8051242058756, s=20, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.5)
    pylab.ylim(0.1, 1000)
    pylab.show()

    t_list = [0.01 * i for i in range(20000)]
    pylab.plot(t_list, y_lists[0], t_list, y_lists[1])
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()
    """
    y_lists = []

    result = runge_cutt_noise((1.5766958463682283, 18.12474133000354), mu=0.013, epsilon=0.0002, points_count=30000)
    pylab.plot(*result, zorder=2)
    y_lists.append(result[1])

    result = runge_cutt_noise((1.5766958463682283, 18.12474133000354), mu=0.013, epsilon=0.0005, points_count=30000)
    pylab.plot(*result, zorder=1)
    y_lists.append(result[1])

    result = separatrix(mu=0.013)
    pylab.plot(*result, zorder=1, color='red', linewidth=2, linestyle='dashed')
    pylab.scatter(1.5502109282783596, 26.219153949156567, s=20, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 2.0)
    pylab.ylim(10, 1000)
    pylab.show()

    t_list = [0.01 * i for i in range(30000)]
    pylab.plot(t_list, y_lists[0], t_list, y_lists[1])
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()


if __name__ == '__main__':
    figure_5()

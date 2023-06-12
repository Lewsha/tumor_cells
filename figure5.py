"""Построение figure 5 для отчета"""
import pylab
from main_functions import *
from separatrix import separatrix
from resting_points_calculation import resting_points_calc


def figure_5():

    '''y_lists = []

    result = runge_cutt_noise((0.29054078392006955, 411.20391689484427), mu=0.0027, epsilon=0.0002, points_count=20000)
    pylab.plot(*result, zorder=2, linewidth=2, label=r'$\epsilon$ = 0.0002')
    y_lists.append(result[1])

    result = runge_cutt_noise((0.29054078392006955, 411.20391689484427), mu=0.0027, epsilon=0.0005, points_count=20000)
    pylab.plot(*result, zorder=1, linewidth=2, label=r'$\epsilon$ = 0.0005')
    y_lists.append(result[1])

    result = separatrix(mu=0.0027)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(0.5208856335983751, 340.8051242058756, s=50, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.legend(loc=0, fontsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.5)
    pylab.ylim(0.1, 1000)

    points = resting_points_calc(mu=0.0027)
    pylab.scatter(points[0][0], points[0][1], s=20, zorder=2, color='black')
    pylab.scatter(points[1][0], points[1][1], s=20, zorder=2, color='black')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0] + 0.1, points[0][1] - 10), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0] + 0.1, points[2][1] - 10), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0] + 0.1, points[1][1] + 5), fontsize=30)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    pylab.show()

    t_list = [0.01 * i for i in range(20000)]
    pylab.plot(t_list, y_lists[0], linewidth=2, label=r'$\epsilon$ = 0.0002')
    pylab.plot(t_list, y_lists[1], linewidth=2, label=r'$\epsilon$ = 0.0005')
    pylab.tick_params(axis='both', which='major', labelsize=20)

    ax = pylab.gca()
    ax.set_xlabel("t", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    pylab.legend(loc=0, fontsize=20)
    pylab.xlim(0.0, 200)

    pylab.show()'''

    y_lists = []

    result = runge_cutt_noise((1.5766958463682283, 18.12474133000354), mu=0.013, epsilon=0.0002, points_count=30000)
    pylab.plot(*result, zorder=2, linewidth=2, label=r'$\epsilon$ = 0.0002')
    y_lists.append(result[1])

    result = runge_cutt_noise((1.5766958463682283, 18.12474133000354), mu=0.013, epsilon=0.0005, points_count=30000)
    pylab.plot(*result, zorder=1, linewidth=2, label=r'$\epsilon$ = 0.0005')
    y_lists.append(result[1])

    result = separatrix(mu=0.013)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(1.5502109282783596, 26.219153949156567, s=50, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 2.0)
    pylab.ylim(10, 1000)

    points = resting_points_calc(mu=0.013)
    pylab.scatter(points[0][0], points[0][1], s=20, zorder=2, color='black')
    pylab.scatter(points[1][0], points[1][1], s=20, zorder=2, color='black')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0] + 0.1, points[0][1] - 10), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0] + 0.01, points[2][1] + 5), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0] + 0.1, points[1][1]), fontsize=30)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)
    pylab.legend(loc=0, fontsize=20)

    pylab.show()

    t_list = [0.01 * i for i in range(30000)]
    pylab.plot(t_list, y_lists[0], linewidth=2, label=r'$\epsilon$ = 0.0002')
    pylab.plot(t_list, y_lists[1], linewidth=2, label=r'$\epsilon$ = 0.0005')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.xlim(0.0, 200)
    pylab.legend(loc=0, fontsize=20)

    ax = pylab.gca()
    ax.set_xlabel("t", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.99)

    pylab.show()


if __name__ == '__main__':
    figure_5()

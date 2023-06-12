"""Построение figure 3 для отчета"""
import pylab
from main_functions import *
from separatrix import separatrix
from resting_points_calculation import resting_points_calc


# 0.0026 - без сепаратрисы, 0.0027+, 0.005+, 0.008+, 0.0013, 0.0014 - без сепаратрисы
# 0.0002, 0.0005


def figure_3():

    start_points_0026 = [(0.00001, 100), (0.7, 1000), (0.5, 0.1), (2.5, 1000)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_0026)):
        print(point_number)
        result = runge_cutt(start_points_0026[point_number], mu=0.0026)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.5)
    pylab.ylim(0.1, 1000)
    pylab.show()



    start_points_0027 = [(0.00001, 100), (0.7, 1000), (0.53, 338), (0.515, 342), (0.5, 0.1), (2.5, 1000)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_0027)):
        print(point_number)
        result = runge_cutt(start_points_0027[point_number], mu=0.0027)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    result = separatrix(mu=0.0027)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(0.5208856335983751, 340.8051242058756, s=50, zorder=2, edgecolors='black', color='w')

    points = resting_points_calc(mu=0.0027)
    pylab.scatter(points[0][0], points[0][1], s=20, zorder=2, color='black')
    pylab.scatter(points[1][0], points[1][1], s=20, zorder=2, color='black')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0] + 0.1, points[0][1] - 10), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0] + 0.1, points[2][1] - 10), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0] + 0.1, points[1][1] + 5), fontsize=30)

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.5)
    pylab.ylim(0.1, 1000)
    pylab.show()



    start_points_005 = [(2.5, 1000), (3.2, 750), (1.17, 140), (1.16, 145), (0.001, 1), (3.2, 650)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_005)):
        print(point_number)
        result = runge_cutt(start_points_005[point_number], mu=0.005)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    result = separatrix(mu=0.005)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(1.1656679694642182, 143.74450810995776, s=50, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.2)
    pylab.ylim(1, 1000)
    pylab.show()


    start_points_008 = [(2.5, 1000), (3.2, 1.4), (1.40, 74), (1.38, 76), (0.5, 0.2), (3.2, 650)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_008)):
        print(point_number)
        result = runge_cutt(start_points_008[point_number], mu=0.008)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    result = separatrix(mu=0.008)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(1.389523555054411, 75.32898684156143, s=50, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 3.2)
    pylab.ylim(0.2, 1000)
    pylab.show()


    start_points_013 = [(2.5, 1000), (2.0, 47), (1.55, 26.3), (1.555, 26.05), (0.5, 10), (2.0, 55)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_013)):
        print(point_number)
        result = runge_cutt(start_points_013[point_number], mu=0.013)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    result = separatrix(mu=0.013)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.scatter(1.5502109282783596, 26.219153949156567, s=50, zorder=2, edgecolors='black', color='w')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 2.0)
    pylab.ylim(10, 1000)
    pylab.show()


    start_points_014 = [(0.5, 10), (2.0, 1000), (2.0, 50), (2.0, 150), (1, 10)]
    x_lists = []
    y_lists = []
    for point_number in range(len(start_points_014)):
        print(point_number)
        result = runge_cutt(start_points_014[point_number], mu=0.014)
        x_lists.append(result[0])
        y_lists.append(result[1])
    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.plot(*result, linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.0, 2.0)
    pylab.ylim(10, 1000)
    pylab.show()


if __name__ == '__main__':
    figure_3()

'''Доверительные эллипсы'''
import pylab
from main_functions import *
from resting_points_calculation import resting_points_calc
from separatrix import separatrix
import math
from numpy.linalg import eig
import numpy


def noise_activity_diagram(*args, mu=0.00311, mode=0):
    """Временные ряды для оценки перемещения кривых при разных уравнях шума"""

    result = runge_cutt([2, 8])

    x_start = result[0][-1]
    y_start = result[1][-1]

    t_list = [0.01 * i for i in range(1000000)]
    if mode == 1:
        # print(args)
        for arr in args:
            pylab.plot(t_list[0:len(arr[1])], arr[1], label='epsilon = {}'.format(arr[2]))
            pylab.legend(loc=0, fontsize=20)
    else:
        for epsilon in [0.1, 0.3]:
            result = runge_cutt_noise([x_start, y_start], points_count=50000, epsilon=epsilon, mu=mu)
            # Нарисуем одномерный график
            pylab.plot(t_list, result[1], label='epsilon = {}'.format(epsilon))
            pylab.legend(loc=0, fontsize=20)

    # Покажем окно с нарисованным графиком
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()


def trust_ellipse(x, y, s1, s2, P, epsilon, mu=mu):
    """Реализация фукнции стохастической чувствительности
    при помощи метода Крамера, возвращающая координаты доверительного эллипса"""
    fx = ((row * y) / (eta + y) - mu * y - delta)
    fy = ((row * eta * x) / (eta + y) ** 2 - mu * x)
    gx = (-1 * y)
    gy = (alfa - 2 * alfa * beta * y - x)

    delta0 = 2*fx*2*gy*(fx+gy) - (2*fx*2*gx*fy + 2*fy*gx*2*gy)
    # delta1 = -1*s1*(fx+gy)*2*gy - s2*2*fy*2*gy - (-1*s1*2*gx*fy)
    delta1 = -1*s1*(fx+gy)*2*gy - s2*2*fy*fy - (-1*s1*2*gx*fy)
    delta2 = -1*(-1*s1*gx*2*gy - s2*fy*2*fx)
    delta3 = -1*s2*2*fx*(fx+gy) - s1*gx*2*gx - (-1*s2*2*fx*gx)

    a = delta1/delta0
    b = delta2/delta0
    c = delta3/delta0
    # print(a, b, c)

    matrix = numpy.matrix(f'{a}, {b}; {b}, {c}')
    data = eig(matrix)
    roots = data[0]
    vectors = data[1]
    # print('roots', roots)
    # print(vectors)
    vectors = list(numpy.array(data[1]))

    v1_len = math.sqrt(vectors[0][0]**2 + vectors[1][0]**2)
    v2_len = math.sqrt(vectors[0][1]**2 + vectors[1][1]**2)

    v11 = vectors[0][0]
    v12 = vectors[1][0]
    v21 = vectors[0][1]
    v22 = vectors[1][1]
    # print(v11, v12, v21, v22)

    k = math.sqrt(-1 * math.log(1 - P))

    rad_step = 0.00872665

    rad_list = [rad_step*i for i in range(720)]
    x_list_el = []
    y_list_el = []

    for rad in rad_list:
        z1 = epsilon * k * math.sqrt(2*roots[0]) * math.cos(rad)
        z2 = epsilon * k * math.sqrt(2*roots[1]) * math.sin(rad)

        x_list_el.append(x + (z1*v22 - z2*v12)/(v11*v22 - v12*v21))
        y_list_el.append(y + (z2*v11 - z1*v21)/(v11*v22 - v12*v21))

    return x_list_el, y_list_el


def noise_activity(x, y, mu, epsilon, P):
    points = resting_points_calc(mu=mu)
    x_list, y_list = runge_cutt_noise((x, y), mu=mu, points_count=500000, epsilon=epsilon, h=0.001)
    x_list_plot = x_list[::10]
    y_list_plot = y_list[::10]

    ellips = trust_ellipse(x, y, x**2 * y**2, 0, P, epsilon=epsilon, mu=mu)
    pylab.plot(ellips[0], ellips[1], zorder=1)
    pylab.tick_params(axis='both', which='major', labelsize=20)

    pylab.plot(x_list_plot, y_list_plot, color='dimgray', zorder=1)
    sep = separatrix(mu=mu)
    pylab.plot(*sep, color='red', zorder=1, linewidth=5)
    pylab.scatter([points[0][0], points[1][0]],
                  [points[0][1], points[1][1]], s=50, zorder=2, color='black')
    pylab.scatter(points[2][0], points[2][1], s=50, zorder=2, edgecolors='black', color='w')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0]+0.1, points[0][1]-50), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0]+0.1, points[1][1]-50), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0]+0.1, points[2][1]-30), fontsize=30)
    pylab.xlim(0, 2)
    pylab.ylim(0, 500)
    # pylab.yscale('log')
    pylab.show()
    noise_activity_diagram((x_list, y_list, epsilon), mode=1)


def points_in_ellipse(x, y, mu, epsilon, P):
    points = resting_points_calc(mu=mu)
    x_list1, y_list1 = runge_cutt_noise((x, y), mu=mu, points_count=500000, epsilon=epsilon, h=0.01)
    ellips = trust_ellipse(x, y, x ** 2 * y ** 2, 0, P, epsilon=epsilon, mu=mu)
    pylab.plot(ellips[0], ellips[1], zorder=1)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    res = [[], []]
    for i in range(0, len(x_list1), 100):
        res[0].append(x_list1[i])
        res[1].append(y_list1[i])
    pylab.scatter(res[0], res[1], s=20, color='black')
    pylab.show()


def ellipses(x, y, epsilon1, epsilon2, P, mu=mu):
    """Функция для отрисовки двух доверительных эллипсов с разным уровнем шума"""
    points = resting_points_calc(mu=mu)
    ellips1 = trust_ellipse(x, y, x**2 * y**2, 0, P, epsilon=epsilon1, mu=mu)
    ellips2 = trust_ellipse(x, y, x**2 * y**2, 0, P, epsilon=epsilon2, mu=mu)
    sep = separatrix(mu=mu)
    pylab.plot(*sep, color='red', zorder=1, linewidth=2, linestyle='dashed')
    pylab.plot(*ellips1, color='dimgray', zorder=1)
    pylab.plot(*ellips2, color='brown', zorder=1)
    pylab.scatter(points[2][0], points[2][1], s=50, zorder=2, edgecolors='black', color='w')
    pylab.scatter(x, y, s=50, zorder=2, edgecolors='black', color='black')
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0]+0.1, points[2][1]-30), fontsize=30)
    pylab.annotate('B', xy=(x, y), xytext=(x+0.05, y+2), fontsize=30)
    pylab.yscale('log')
    pylab.xlim(0, 1.5)
    pylab.ylim(200, 500)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()


if __name__ == "__main__":
    points = resting_points_calc(mu=0.0027)
    # noise_activity_diagram()
    # print(points)
    # noise_activity(points[1][0], points[1][1], 0.005, 0.01, 0.95)
    ellipses(points[0][0], points[0][1], 0.0001, 0.0005, 0.99, mu=0.0027)

import math
import random
import pylab
from drug_separatrix import drug_separatrix

"""Константы, входящие в оригинальную систуму ДУ"""
sigma = 0.1181
row = 1.131
eta = 20.19
delta = 0.3743
alfa = 1.636
beta = 0.002
mu = 0.00311

b = 1.35

'''
b_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
          1.05, 1.1, 1.2, 1.3, 1.325, 1.35]  # b - воздействие лекарств
'''
b_list = [0.2, 0.9, 1.0, 1.2, 1.4, 12]


def f(x, y, sigma=sigma, row=row, eta=eta, delta=delta, mu=mu):
    """Исходная функция f системы ДУ"""
    return sigma + (row * x * y)/(eta + y) - mu * x * y - delta * x


def g(x, y, alfa=alfa, beta=beta, b=b):
    """Исходная функция g системы ДУ"""
    return alfa * y * (1 - beta * y) - x * y - ((b*y)/(1+y))


def runge_cutt(point,
               f=f, g=g,
               sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu, b=b,
               points_count=10000, h=0.01):
    """Реализация метода Рунге-Кутты 4-го порядка
    (строит одну кривую и возвращает списки координат точек)"""

    x_list = [point[0]]
    y_list = [point[1]]

    for i in range(1, points_count):
        k1 = h * f(x_list[i - 1], y_list[i - 1],
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l1 = h * g(x_list[i - 1], y_list[i - 1], alfa=alfa, beta=beta, b=b)
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l2 = h * g(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0), alfa=alfa, beta=beta, b=b)
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l3 = h * g(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0), alfa=alfa, beta=beta, b=b)
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3,
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l4 = h * g(x_list[i - 1] + k3, y_list[i - 1] + l3, alfa=alfa, beta=beta, b=b)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)

    return x_list, y_list


def grid_build(mu=0.0027, b=b):
    """Функция для построения "сетки" из набора кривых, исходящих из разных точек"""

    points_dic = {0.1: [[0.29085423107043973, 411.03394574557194],
                        [1.598629627612696, 8.040754470768576],
                        [0.5202135847331949, 340.9211339128284]],
                  0.2: [[0.2911694704689477, 410.8633654020245],
                        [1.5875848247925926, 8.020965777117596],
                        [0.5195397678125769, 341.0377449265783]],
                  0.9: [[0.2934283466282672, 409.6515936701903],
                        [1.5088033029185244, 7.872395529938871],
                        [0.5147715281675813, 341.8715103388879]],
                  1.0: [[0.29375880452697795, 409.4758553142504],
                        [1.497316470379507, 7.849580960334805],
                        [0.5140826870491458, 341.99321619599243]],
                  1.2: [[0.2944258104035499, 409.12232068065646],
                        [1.474146649287272, 7.802609455398141],
                        [0.512698987904191, 342.2386621156887]]
                  }
    # points = points_dic[b]
    # points = points_dic[1.0]

    # new_x = 0.1
    # new_y = 0.1
    # grid = [(new_x, new_y)]

    new_y = 0.1
    grid = []
    x_lists = []
    y_lists = []

    new_y = 0.1
    yy = [0.1, 10, 100, 500]
    for i in range(4):
        new_x = 0
        for j in range(4):
            grid.append([new_x, new_y])
            new_x += 0.5
        # new_y += 200
        new_y += yy[i]

    # grid.append([points[1][0] - 0.1, points[1][1]])

    for point_number in range(len(grid)):
        print(point_number)
        result = runge_cutt(grid[point_number], mu=mu, points_count=100000, b=b)
        x_lists.append(result[0])
        y_lists.append(result[1])

    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    # Нарисуем двумерный график
    pylab.plot(*result, zorder=1, linewidth=2)
    '''pylab.scatter([points[0][0], points[1][0]],
                  [points[0][1], points[1][1]], s=50, zorder=3, color='black')
    pylab.scatter(points[2][0], points[2][1], s=50, zorder=3, edgecolors='black', color='w')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0] + 0.1, points[0][1] - 50), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0] + 0.1, points[1][1] + 10), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0] + 0.1, points[2][1] - 30), fontsize=30)'''
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')

    pylab.annotate('A', xy=(sigma/delta, 0.001), xytext=(sigma/delta - 0.2, 0.001), fontsize=20)

    result = drug_separatrix(b=b)
    pylab.plot(*result, zorder=1, color='red', linewidth=5, linestyle='dashed')
    pylab.xlim(0, 4)
    # pylab.ylim(0.00001, 500)

    ax = pylab.gca()
    ax.set_xlabel("x", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    # Покажем окно с нарисованным графиком
    pylab.show()


if __name__ == "__main__":
    '''b_list = [0.2, 0.9, 1.0, 1.2, 1.4]
    b_list = [1.4]
    for i in range(len(b_list)):
        print(b_list[i])
        grid_build(mu=0.0027, b=b_list[i])'''

    grid_build(mu=0.0027, b=1.4)

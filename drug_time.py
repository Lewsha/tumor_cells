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


def time_build(mu=0.0027, b=b):
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
    points = points_dic[1.0]

    grid = [[1.5, 100]]
    t_list = [0.01 * i for i in range(100000)]
    result = runge_cutt([1.5, 100], mu=mu, points_count=100000, b=b)
    pylab.plot(t_list, result[1], linewidth=2)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    ax = pylab.gca()
    ax.set_xlabel("t", fontsize=20, color='black')
    ax.set_ylabel("y", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    pylab.xlim(0.0, 1000)
    pylab.ylim(0.0, 99)

    pylab.show()


if __name__ == "__main__":
    time_build(b=0.98)

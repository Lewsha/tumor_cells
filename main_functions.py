"""Реализация осноных необходимых функций
(численный метод Рунге-Кутты 4 порядка,
вариант метода с шумом, функции f и g системы ДУ, математические константы и т.д."""

import math
import random

"""Константы, входящие в оригинальную систуму ДУ"""
sigma = 0.1181
row = 1.131
eta = 20.19
delta = 0.3743
alfa = 1.636
beta = 0.002
mu = 0.00311

b = 0  # Воздействие лекарств


def f(x, y, sigma=sigma, row=row, eta=eta, delta=delta, mu=mu):
    """Исходная функция f системы ДУ"""
    return sigma + (row * x * y)/(eta + y) - mu * x * y - delta * x


def g(x, y, alfa=alfa, beta=beta):
    """Исходная функция g системы ДУ"""
    return alfa * y * (1 - beta * y) - x * y


def g_drugs(x, y, alfa=alfa, beta=beta, b=b):
    """Исходная функция g системы ДУ"""
    return alfa * y * (1 - beta * y) - x * y - ((b*y)/(1+y))


def runge_cutt(point,
               f=f, g=g,
               sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu,
               points_count=10000, h=0.01):
    """Реализация метода Рунге-Кутты 4-го порядка
    (строит одну кривую и возвращает списки координат точек)"""

    x_list = [point[0]]
    y_list = [point[1]]

    for i in range(1, points_count):
        k1 = h * f(x_list[i - 1], y_list[i - 1],
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l1 = h * g(x_list[i - 1], y_list[i - 1], alfa=alfa, beta=beta)
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l2 = h * g(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0), alfa=alfa, beta=beta)
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l3 = h * g(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0), alfa=alfa, beta=beta)
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3,
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l4 = h * g(x_list[i - 1] + k3, y_list[i - 1] + l3, alfa=alfa, beta=beta)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)

    return x_list, y_list


def runge_cutt_noise(point,
                     f=f, g=g,
                     sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu,
                     points_count=100000, h=0.01,
                     epsilon=0.001):
    """Реализация метода Рунге-Кутты 4-го порядка с добавлением шума
    (строит одну кривую и возвращает списки координат точек)"""
    x_list = [point[0]]
    y_list = [point[1]]

    for i in range(1, points_count):
        k1 = h * f(x_list[i - 1], y_list[i - 1],
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l1 = h * g(x_list[i - 1], y_list[i - 1], alfa=alfa, beta=beta)
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l2 = h * g(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0), alfa=alfa, beta=beta)
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l3 = h * g(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0), alfa=alfa, beta=beta)
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3,
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l4 = h * g(x_list[i - 1] + k3, y_list[i - 1] + l3, alfa=alfa, beta=beta)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)) - \
             epsilon * random.gauss(0, 1) * math.sqrt(h) * x_list[i - 1] * y_list[i - 1]
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)

    return x_list, y_list


def runge_cutt_drugs(point,
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
        l1 = h * g_drugs(x_list[i - 1], y_list[i - 1], alfa=alfa, beta=beta, b=b)
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l2 = h * g_drugs(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0), alfa=alfa, beta=beta, b=b)
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l3 = h * g_drugs(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0), alfa=alfa, beta=beta, b=b)
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3,
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l4 = h * g_drugs(x_list[i - 1] + k3, y_list[i - 1] + l3, alfa=alfa, beta=beta, b=b)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4))
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)

    return x_list, y_list


def runge_cutt_noise_drugs(point,
               f=f, g=g,
               sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu, b=b,
               points_count=10000, h=0.01, epsilon=0.001):
    """Реализация метода Рунге-Кутты 4-го порядка
    (строит одну кривую и возвращает списки координат точек)"""

    x_list = [point[0]]
    y_list = [point[1]]

    for i in range(1, points_count):
        k1 = h * f(x_list[i - 1], y_list[i - 1],
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l1 = h * g_drugs(x_list[i - 1], y_list[i - 1], alfa=alfa, beta=beta, b=b)
        k2 = h * f(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l2 = h * g_drugs(x_list[i - 1] + (k1 / 2.0), y_list[i - 1] + (l1 / 2.0), alfa=alfa, beta=beta, b=b)
        k3 = h * f(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0),
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l3 = h * g_drugs(x_list[i - 1] + (k2 / 2.0), y_list[i - 1] + (l2 / 2.0), alfa=alfa, beta=beta, b=b)
        k4 = h * f(x_list[i - 1] + k3, y_list[i - 1] + l3,
                   sigma=sigma, row=row, eta=eta, delta=delta, mu=mu)
        l4 = h * g_drugs(x_list[i - 1] + k3, y_list[i - 1] + l3, alfa=alfa, beta=beta, b=b)
        xm = x_list[i - 1] + ((1.0 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)) - \
             epsilon * random.gauss(0, 1) * math.sqrt(h) * x_list[i - 1] * y_list[i - 1]
        ym = y_list[i - 1] + ((1.0 / 6) * (l1 + 2.0 * l2 + 2.0 * l3 + l4))
        # print(xm, '\t', ym)
        x_list.append(xm)
        y_list.append(ym)

    return x_list, y_list


def roots_of_quadratic_equation(a, b, c):
    """Функция для нахождения корней квадратного уравнения"""
    D = b ** 2 - 4 * a * c  # дискриминант
    # print("Дискриминант: ", D)
    x1 = (-b + D ** 0.5) / (2 * a)  # первый корень
    x2 = (-b - D ** 0.5) / (2 * a)  # второй корень
    return x1, x2

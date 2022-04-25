from main_functions import *
import numpy
from scipy.special import cbrt
import pylab
from numpy.linalg import eig


def resting_points_calc_drugs(sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu):
    """ПРОВЕРЕНО, РАБОТАЕТ ВЕРНО"""
    """Функция вычисления точек покоя из кубического уравнения на основе формулы Кардано"""
    """(mu*alfa*beta)*y**3 + 
    (-1*row*alfa*beta - mu*alfa + mu*alfa*beta*eta + delta*alfa*beta)*y**2 + 
    (sigma + row*alfa - mu*alfa*eta - delta*alfa + delta*alfa*beta*eta)*y + 
    (sigma*eta - delta*alfa*eta) = 0"""

    a = mu * alfa * beta
    b = -1 * row * alfa * beta - mu * alfa + mu * alfa * beta * eta + delta * alfa * beta
    c = sigma + row * alfa - mu * alfa * eta - delta * alfa + delta * alfa * beta * eta
    d = sigma * eta - delta * alfa * eta

    """
    Подстановочные данные для проверки
    a = 1
    b = -6
    c = 11
    d = -6
    """

    # print(a, b, c, d)
    # print()

    a, b, c, d = a+0j, b+0j, c+0j, d+0j
    all_ = (a != numpy.pi)

    Q = (3*a*c - b**2) / (9*a**2)
    R = (9*a*b*c - 27*a**2*d - 2*b**3) / (54 * a**3)
    D = Q**3 + R**2
    S = 0  # NEW CALCULATION FOR S STARTS HERE
    if numpy.isreal(R + numpy.sqrt(D)):
        S = cbrt(numpy.real(R + numpy.sqrt(D)))
    else:
        S = (R + numpy.sqrt(D))**(1/3)
    T = 0  # NEW CALCULATION FOR T STARTS HERE
    if numpy.isreal(R - numpy.sqrt(D)):
        T = cbrt(numpy.real(R - numpy.sqrt(D)))
    else:
        T = (R - numpy.sqrt(D))**(1/3)

    y_list = list()
    y_list.append(- b / (3*a) + (S+T))
    y_list.append(- b / (3*a) - (S+T) / 2 + 0.5j * numpy.sqrt(3) * (S - T))
    y_list.append(- b / (3*a) - (S+T) / 2 - 0.5j * numpy.sqrt(3) * (S - T))
    x_list = [alfa - alfa*beta*y for y in y_list]

    return [(x_list[i], y_list[i]) for i in range(3)]

if __name__ == '__main__':
    print(resting_points_calc_drugs())
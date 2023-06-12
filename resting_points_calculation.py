from main_functions import *
import numpy
from scipy.special import cbrt
import pylab
from numpy.linalg import eig


def resting_points_calc(sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu):
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


def resting_points_analysis(x, y, sigma=sigma, row=row, eta=eta, delta=delta, alfa=alfa, beta=beta, mu=mu):
    """Функция для вычисления коэффициентов lambda (для оценки устойчивости),
    (матрица стохастической чувствительности)"""
    # s1 = 1
    s1 = x**2 * y**2
    s2 = 0
    fx = ((row * y) / (eta + y) - mu * y - delta)
    fy = ((row * eta * x) / (eta + y) ** 2 - mu * x)
    gx = (-1 * y)
    gy = (alfa - 2 * alfa * beta * y - x)

    delta0 = 2 * fx * 2 * gy * (fx + gy) - (2 * fx * 2 * gx * fy + 2 * fy * gx * 2 * gy)
    delta1 = -1 * s1 * (fx + gy) * 2 * gy - s2 * 2 * fy * fy - (-1 * s1 * 2 * gx * fy)
    delta2 = -1 * (-1 * s1 * gx * 2 * gy - s2 * fy * 2 * fx)
    delta3 = -1 * s2 * 2 * fx * (fx + gy) - s1 * gx * 2 * gx - (-1 * s2 * 2 * fx * gx)

    a = delta1 / delta0
    b = delta2 / delta0
    c = delta3 / delta0

    matrix = numpy.matrix(f'{a}, {b}; {b}, {c}')
    data = eig(matrix)
    roots = data[0]

    return roots


def resting_points_change_character():
    """Функция, позволяющая посмотреть изменение
    характера точки покоя при изменении коэффициента mu в исходном уравнении"""
    mu_list = [0.002633 + i*0.0001 for i in range(105)]
    # mu_list.append(0.01323)
    print(mu_list)
    names = ['Точка B', 'Точка G', 'Точка S']
    colors = ['navy', 'forestgreen', 'purple']
    x1 = mu_list[0]
    x2 = mu_list[-1]
    max_y1 = 0
    max_y2 = 0
    for i in range(0, 2):
        lambda_list1 = []
        lambda_list2 = []
        for j in range(105):
            points = resting_points_calc(mu=mu_list[j])
            lambdas = resting_points_analysis(points[i][0], points[i][1], mu=mu_list[j])
            # print(lambdas)
            lambda_list1.append((lambdas[0]))
            lambda_list2.append((lambdas[1]))

        # print(f'point № {i}')
        # print(lambda_list1)
        # print()
        # print(lambda_list2)
        # print()
        # print()
        # print()
        pylab.plot(mu_list, lambda_list1, mu_list, lambda_list2, label='{}'.format(names[i]), color=colors[i],
                   linewidth=3)
        pylab.legend()

        max_y1 = max(max_y1, lambda_list1[0], lambda_list2[0])
        max_y2 = max(max_y2, lambda_list1[-1], lambda_list2[-1])

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    pylab.xlim(0.002, 0.0139)

    pylab.plot([x1, x1], [0, max_y1], color='gray', linestyle='dashed', linewidth=2)
    pylab.plot([x2, x2], [0, max_y2], color='gray', linestyle='dashed', linewidth=2)

    ax = pylab.gca()
    ax.set_xlabel(r"$\mu$", fontsize=20, color='black')
    ax.set_ylabel(r"$\lambda$", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.95)

    points = numpy.array([mu_list[0], 0.004, 0.006, 0.008, 0.01, 0.012, mu_list[-1]])
    labels = [r'$\mu_1$', '0.004', '0.006', '0.008', '0.01', '0.012', r'$\mu_2$']
    pylab.xticks(points, labels)

    # Покажем окно с нарисованным графиком
    pylab.show()


if __name__ == '__main__':
    # resting_points = resting_points_calc(mu=0.00311)
    # print(resting_points)
    # print(resting_points_analysis(resting_points[2][0], resting_points[2][1], mu=0.00311))
    # print(roots_of_quadratic_equation(1, 7, 12))
    """for point in resting_points:
        print(point)

    print()

    for point in resting_points:
        print(resting_points_analysis(point[0], point[1], mu=0.01))
    print()"""

    resting_points_change_character()



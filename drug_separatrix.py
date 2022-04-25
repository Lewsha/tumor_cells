"""Черновик под разные вычисления"""
import pylab

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


def drug_separatrix(b=0.2):

    grid = {0.01: ((-0.1, 3.41273), (0.5208185076221241, 340.816698328777), (4, 6539.03294)),
           0.05: ((-0.1, 3.43916), (0.5205498287394934, 340.8630543596746), (4, 6542.18437)),
           0.1: ((-0.1, 3.47227), (0.5202135847331949, 340.9211339128284), (4, 6546.13319)),
           0.2: ((-0.1, 3.53866289), (0.5195397678125769, 341.0377449265783), (4, 6554.062861)),
           0.9: ((-0.1, 4.0100652), (0.5147715281675813, 341.8715103388879), (4, 6610.81141)),
           1.0: ((-0.1, 4.078323468), (0.5140826870491458, 341.99321619599243), (4, 6619.10276)),
           1.2: ((-0.1, 4.21550), (0.512698987904191, 342.2386621156887), (4, 6635.83010)),
           1.4: ((-0.1, 4.35354), (0.5113070746085246, 342.4868821294684), (4, 6652.75481)),
           12: ((-0.1, 13.80543), (0.3996870117410943, 367.90472625937474), (4, 8443.35742))}

    if b not in grid.keys():
        b = 0.2

    x_list = []
    y_list = []

    result = runge_cutt(grid[b][0], mu=0.0027, points_count=2000, b=b)
    x_list.extend(result[0])
    y_list.extend(result[1])

    x_list.append(grid[b][1][0])
    y_list.append(grid[b][1][1])

    result = runge_cutt(grid[b][2], mu=0.0027, points_count=2000, b=b)
    result = list(result)
    result[0].reverse()
    result[1].reverse()
    x_list.extend(result[0])
    y_list.extend(result[1])

    return x_list, y_list


def exsp():

    sep = {0.01: ((-0.1, 3.41273), (0.5208185076221241, 340.816698328777), (4, 6539.03294)),
           0.05: ((-0.1, 3.43916), (0.5205498287394934, 340.8630543596746), (4, 6542.18437)),
           0.1: ((-0.1, 3.47227), (0.5202135847331949, 340.9211339128284), (4, 6546.13319)),
           0.2: ((-0.1, 3.53866289), (0.5195397678125769, 341.0377449265783), (4, 6554.062861)),
           0.9: ((-0.1, 4.0100652), (0.5147715281675813, 341.8715103388879), (4, 6610.81141)),
           1.0: ((-0.1, 4.078323468), (0.5140826870491458, 341.99321619599243), (4, 6619.10276)),
           1.2: ((-0.1, 4.21550), (0.512698987904191, 342.2386621156887), (4, 6635.83010)),
           1.4: ((-0.1, 4.35354), (0.5113070746085246, 342.4868821294684), (4, 6652.75481)),
           12: ((-0.1, 13.80543), (0.3996870117410943, 367.90472625937474), (4, 8443.35742))}

    x_lists = [0.5208185076221241, 0.5205498287394934, 0.5202135847331949,
               0.5195397678125769, 0.5147715281675813, 0.5140826870491458,
               0.512698987904191, 0.5113070746085246, 0.3996870117410943]
    y_lists = [340.816698328777, 340.8630543596746, 340.9211339128284,
               341.0377449265783, 341.8715103388879, 341.99321619599243,
               342.2386621156887, 342.4868821294684, 367.90472625937474]

    new_x = 4
    new_y = 6546.13319
    grid = [(new_x, new_y)]

    for i in range(10):
        # new_x += 0.1
        new_y += 0.00001
        grid.append([new_x, new_y])

    x_lists = []
    y_lists = []

    for point_number in range(len(grid)):
        print(point_number)
        result = runge_cutt(grid[point_number], mu=0.0027, points_count=2000, b=0.1)
        x_lists.append(result[0])
        y_lists.append(result[1])

    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    pylab.scatter(0.5202135847331949, 340.9211339128284, s=3, zorder=2)
    pylab.plot(*result, zorder=1)
    pylab.yscale('log')
    pylab.show()


if __name__ == "__main__":
    # Нарисуем двумерный график

    '''res = separatrix(mu=0.00311)
    pylab.plot(res[0], res[1])
    pylab.tick_params(axis='both', which='major', labelsize=20)
    # Покажем окно с нарисованным графиком
    pylab.show()'''
    # print(resting_points_calculation.resting_points_calc(mu=0.013))

    exsp()

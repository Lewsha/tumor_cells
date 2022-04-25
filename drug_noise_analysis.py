"""Доверительные эллипсы для лекарств"""
from numpy.linalg import eig
import numpy
from drug_separatrix import drug_separatrix
import pylab
from main_functions import *


y_lists = [[340.816698328777, 8.058286127809197, 411.18694698259463, -0.992672179921783],
           [340.8630543596746, 8.05052630748682, 411.1190070057004, -0.9633284136026816],
           [340.9211339128284, 8.040754470768576, 411.03394574557194, -0.9265748699098992],
           [341.0377449265783, 8.020965777117596, 410.8633654020245, -0.8528168464613373],
           [341.8715103388879, 7.872395529938871, 409.6515936701903, -0.3262402797579682],
           [341.99321619599243, 7.849580960334805, 409.4758553142504, -0.24939321131853376],
           [342.2386621156887, 7.802609455398141, 409.12232068065646, -0.09433299248425442],
           [342.4868821294684, 7.753729838760535, 408.7659803185803, 0.06266697244979014],
           [377.5720937657258, 367.90472625937474, 6.796219617079231+4.424536730688678j,
            6.796219617079231-4.424536730688678j]]

x_lists = [[0.5208185076221241, 1.6085293261949871, 0.2905720486367612, 0.2745856963422685],
           [0.5205498287394934, 1.604134137326, 0.2906972848987737, 0.2756985875765092],
           [0.5202135847331949, 1.598629627612696, 0.29085423107043973, 0.2771002197610019],
           [0.5195397678125769, 1.5875848247925926, 0.2911694704689477, 0.2799392493734292],
           [0.5147715281675813, 1.5088033029185244, 0.2934283466282672, 0.3012796796135661],
           [0.5140826870491458, 1.497316470379507, 0.29375880452697795, 0.3045605446407478],
           [0.512698987904191, 1.474146649287272, 0.2944258104035499, 0.311318357538589],
           [0.5113070746085246, 1.4506979696732616, 0.2951011281342861, 0.3183549312548442],
           [0.3688860516881936, 0.3996870117410943, (0.4495334313581578+0.6462502583209729j),
            (0.4495334313581578-0.6462502583209729j)]]

b_list = [0.01, 0.05, 0.1, 0.2, 0.9, 1.0, 1.2, 1.4, 12]


def noise_activity_diagram(*args, mu=0.0027, b=0.2, mode=0):
    """Временные ряды для оценки перемещения кривых при разных уравнях шума"""

    result = runge_cutt([2, 8])

    x_start = result[0][-1]
    y_start = result[1][-1]

    t_list = [0.01 * i for i in range(1000000)]
    if mode == 1:
        colors = ['darkorange', 'navy']
        i = 0
        # print(args)
        for arr in args:
            pylab.plot(t_list[0:len(arr[1])], arr[1], color=colors[i % 2], label='epsilon = {}'.format(arr[2]))
            pylab.legend(loc=0, fontsize=20)
            i += 1
    else:
        for epsilon in [0.1, 0.3]:
            result = runge_cutt_noise_drugs([x_start, y_start], points_count=50000, epsilon=epsilon, mu=mu, b=b)
            # Нарисуем одномерный график
            pylab.plot(t_list, result[1], label='epsilon = {}'.format(epsilon))
            pylab.legend(loc=0, fontsize=20)

    # Покажем окно с нарисованным графиком
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()


def trust_ellipse(x, y, s1, s2, P, epsilon, mu=0.0027, b=0.2):
    """Реализация фукнции стохастической чувствительности
    при помощи метода Крамера, возвращающая координаты доверительного эллипса"""
    fx = ((row*y)/(eta + y) - mu*y - delta)
    fy = ((row*eta*x)/((eta + y)**2) - mu*x)
    gx = (-1*y)
    gy = (alfa - 2*alfa*beta*y - x - (b/((1+y)**2)))

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


def noise_activity(x, y, mu, b, epsilons, P):

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
    points = points_dic[b]

    args = []
    priority = len(epsilons)
    colors = ['darkorange', 'navy']
    i = 0
    for epsilon in epsilons:
        x_list, y_list = runge_cutt_noise_drugs((x, y), mu=mu, points_count=500000, epsilon=epsilon, h=0.001, b=b)
        x_list_plot = x_list[::10]
        y_list_plot = y_list[::10]

        ellips = trust_ellipse(x, y, x ** 2 * y ** 2, 0, P, epsilon=epsilon, mu=mu)
        pylab.plot(ellips[0], ellips[1], zorder=len(epsilons)+1, color='red')

        pylab.plot(x_list_plot, y_list_plot, color=colors[i % 2], label='epsilon = {}'.format(epsilon), zorder=priority)
        priority -= 1
        i += 1

        args.append((x_list, y_list, epsilon))

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.legend(loc=0, fontsize=20)

    sep = drug_separatrix(b=b)
    pylab.plot(*sep, color='red', zorder=len(epsilons)+1, linewidth=3, linestyle='dashed')
    pylab.scatter([points[0][0], points[1][0]],
                  [points[0][1], points[1][1]], s=50, zorder=len(epsilons)+1, color='black')
    pylab.scatter(points[2][0], points[2][1], s=50, zorder=len(epsilons)+2, edgecolors='black', color='w')
    pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0]+0.1, points[0][1]-50), fontsize=30)
    pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0]+0.1, points[1][1]+50), fontsize=30)
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0]+0.1, points[2][1]-30), fontsize=30)
    pylab.xlim(0, 4)
    pylab.ylim(0, 600)
    # pylab.yscale('log')
    pylab.show()
    noise_activity_diagram(*args, mode=1)


def points_in_ellipse(x, y, mu, b, epsilon, P):
    x_list1, y_list1 = runge_cutt_noise_drugs((x, y), mu=mu, points_count=500000, epsilon=epsilon, h=0.01, b=b)
    ellips = trust_ellipse(x, y, x ** 2 * y ** 2, 0, P, epsilon=epsilon, mu=mu, b=b)
    pylab.plot(ellips[0], ellips[1], zorder=1)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    res = [[], []]
    for i in range(0, len(x_list1), 100):
        res[0].append(x_list1[i])
        res[1].append(y_list1[i])
    pylab.scatter(res[0], res[1], s=20, color='black')
    sep = drug_separatrix(b=b)
    pylab.plot(*sep, color='red', zorder=1, linewidth=5)
    pylab.xlim(0, 4)
    pylab.ylim(0, 600)
    pylab.show()


def ellipses(x, y, epsilon1, epsilon2, P, mu=0.0027, b=0.2):
    """Функция для отрисовки двух доверительных эллипсов с разным уровнем шума"""
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
    points = points_dic[b]

    ellips1 = trust_ellipse(x, y, x**2 * y**2, 0, P, epsilon=epsilon1, mu=mu)
    ellips2 = trust_ellipse(x, y, x**2 * y**2, 0, P, epsilon=epsilon2, mu=mu)
    sep = drug_separatrix(b=b)
    pylab.plot(*sep, color='red', zorder=1, linewidth=5)
    pylab.plot(*ellips1, color='dimgray', zorder=1)
    pylab.plot(*ellips2, color='brown', zorder=1)
    pylab.scatter(points[2][0], points[2][1], s=50, zorder=2, edgecolors='black', color='w')
    pylab.scatter(x, y, s=50, zorder=2, edgecolors='black', color='black')
    pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0]+0.1, points[2][1]-30), fontsize=30)
    pylab.annotate('G', xy=(x, y), xytext=(x+0.05, y+2), fontsize=30)
    pylab.xlim(-0.15, 3.4)
    pylab.ylim(0, 500)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.show()


if __name__ == "__main__":
    # points_in_ellipse(0.2911694704689477, 410.8633654020245, 0.0027, 0.2, 0.001, 0.75)
    # 411.18694698259463, 411.1190070057004, 411.03394574557194
    # 0.2905720486367612, 0.2906972848987737, 0.29085423107043973
    noise_activity(0.29085423107043973, 411.03394574557194, 0.0027, 1.2, (0.0002, 0.0006), 0.95)
    # ellipses(0.2911694704689477, 410.8633654020245, 0.0005, 0.001, 0.75)


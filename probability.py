"""График вероятности перехода из одного бассейна притяжения в другой
при разных значениях mu и разных уровнях шума"""
from main_functions import *
from resting_points_calculation import resting_points_calc
import pylab


def one_plot(number):
    mu_list = [0.00264, 0.0027, 0.003, 0.004]
    epsilon_list0 = [0.00001 + 0.0000075 * i for i in range(15)]
    epsilon_list1 = [0.0001 + 0.00002 * i for i in range(15)]
    epsilon_list2 = [0.0003 + 0.0001 * i for i in range(15)]
    epsilon_list3 = [0.001 + 0.00025 * i for i in range(15)]
    epsilon_lists = [epsilon_list0, epsilon_list1, epsilon_list2, epsilon_list3]

    epsilon_list = epsilon_lists[number]
    p_list = []
    for i in range(15):
        print(i)
        points = resting_points_calc(mu=mu_list[number])
        bad_x = points[0][0]
        bad_y = points[0][1]
        good_x = points[1][0]
        good_y = points[1][1]
        n = 0
        for j in range(100):
            print(i, j)
            x_list, y_list = runge_cutt_noise((bad_x, bad_y), epsilon=epsilon_list[i],
                                              h=0.01, points_count=100000, mu=mu_list[number])
            x = x_list[-1]
            y = y_list[-1]
            x_list, y_list = runge_cutt((x, y), mu=mu_list[number])
            x = x_list[-1]
            y = y_list[-1]
            # if abs(good_x - x) < 0.2 and abs(good_y - y) < 60:
            #    n += 1
            if abs(good_x - x) < 0.1 and abs(good_y - y) < 30:
                n += 1
        p_list.append(n / 100)
        print(n / 100)

    with open('probability.txt', mode='a') as file:
        file.write(f'{mu_list[number]}\n')
        file.write(' '.join(map(str, epsilon_list)) + '\n')
        file.write(' '.join(map(str, p_list)) + '\n')

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.xscale('log')
    pylab.xlim(0.000005, 0.5)
    pylab.plot(epsilon_list, p_list)
    pylab.show()


def probability_plot():

    with open('probability.txt', mode='r') as file:
        text = file.readlines()

        i = 0
        while i < len(text):
            mu_value = float(text[i])
            mu_list = [float(x) for x in text[i+1].split()]
            p_list = [float(x) for x in text[i+2].split()]
            pylab.plot(mu_list, p_list, marker='o', label=r'$\mu$' + f'= {mu_value}', linewidth=2)
            i += 3

    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.xscale('log')
    ax = pylab.gca()
    ax.set_xlabel(r'$\epsilon$', fontsize=20, color='black')
    ax.set_ylabel("P", fontsize=20, color='black', rotation=0)
    ax.xaxis.set_label_coords(1.005, -0.007)
    ax.yaxis.set_label_coords(-0.015, 0.98)
    pylab.legend(fontsize=15)
    pylab.xlim(0.000005, 0.008)

    pylab.show()


if __name__ == '__main__':
    # one_plot(0)
    probability_plot()

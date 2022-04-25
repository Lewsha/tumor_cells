from main_functions import *
import numpy
from scipy.special import cbrt
import pylab
from numpy.linalg import eig
import resting_points_calculation


def figure2():

    mu_list = []
    value = 0.001
    mu_list.append(value)
    for i in range(200):
        value += 0.0001
        mu_list.append(round(value, 4))

    mu_list.insert(17, 0.002633)
    mu_list.insert(124, 0.01323)

    x_list_bad = []
    y_list_bad = []
    x_list_good = []
    y_list_good = []
    x_list_separ = []
    y_list_separ = []
    for mu_value in mu_list:
        roots = resting_points_calculation.resting_points_calc(mu=mu_value)
        x_list_bad.append(roots[0][0])
        y_list_bad.append(roots[0][1])
        if mu_value < 0.002633:
            x_list_good.append(roots[0][0])
            y_list_good.append(roots[0][1])
        else:
            x_list_good.append(roots[1][0])
            y_list_good.append(roots[1][1])
        x_list_separ.append(roots[2][0])
        y_list_separ.append(roots[2][1])

        # print(f"mu = {mu_value}, roots = {roots}", '\n')

    mu_list_bad = mu_list[17:]
    y_list_bad = y_list_bad[17:]

    mu_list_good = mu_list[:125]
    y_list_good = y_list_good[:125]

    roots = resting_points_calculation.resting_points_calc(mu=0.000000001)
    mu_list_good.insert(0, 0.000000001)
    y_list_good.insert(0, roots[1][1])
    print(roots)

    mu_list_separ = mu_list[17:125]
    y_list_separ = y_list_separ[17:125]

    pylab.plot(mu_list_bad, y_list_bad, color='red', linewidth=2)
    pylab.plot(mu_list_good, y_list_good, color='blue', linewidth=2)
    pylab.plot(mu_list_separ, y_list_separ, color='black', linewidth=2, linestyle='dashed')
    pylab.plot([0.002633, 0.002633], [0, y_list_bad[0]], color='gray', linestyle='dashed')
    pylab.plot([0.01323, 0.01323], [0, y_list_good[-1]], color='gray', linestyle='dashed')
    pylab.tick_params(axis='both', which='major', labelsize=20)
    # pylab.tick_params(axis='x', which='major', labelsize=15)
    # pylab.xticks([0.002633, 0.005, 0.01, 0.01323, 0.015], ['mu1 = 0.002633', 0.005, 0.01, 'mu2 = 0.01323', 0.015])
    pylab.xticks([0.005, 0.01, 0.015], [0.005, 0.01, 0.015])
    pylab.yscale('log')
    pylab.xlim(0.0, 0.017)
    pylab.ylim(0.1, 600)
    pylab.show()


if __name__ == "__main__":
    figure2()

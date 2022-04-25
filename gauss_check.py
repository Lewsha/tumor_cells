"""Проверка нормального распределения для функции gauss в модуле random"""

import numpy as np
import scipy.stats as stats
import random
import pylab

random_values = sorted([random.gauss(0, 1) for i in range(1000)])
fit = stats.norm.pdf(random_values, np.mean(random_values), np.std(random_values))  # this is a fitting indeed
pylab.plot(random_values, fit, '-o')
# pylab.hist(random_values, normed=True)  # use this to draw histogram of your data
pylab.show()  # use may also need add this

h = [random.gauss(0, 1) for i in range(1000)]
h.sort()
hmean = np.mean(h)
hstd = np.std(h)
pdf = stats.norm.pdf(h, hmean, hstd)
pylab.plot(h, pdf)  # including h here is crucial
pylab.show()

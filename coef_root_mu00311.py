"""Вычисление коэффициентов уравнения 4 степени (с лекарствами)
и значения x по известным значениям y и разным коэффициентам b"""
from main_functions import *


def coefficients(b):
    A = alfa*beta*mu  # y**4
    B = -alfa*beta*row - alfa*mu + alfa*beta*mu + alfa*beta*mu*eta + alfa*beta*delta  # y**3
    C = sigma + alfa*row - alfa*beta*row - alfa*mu - alfa*mu*eta + alfa*beta*mu*eta + b*mu - \
        alfa*delta + alfa*beta*delta + alfa*beta*delta*eta  # y**2
    D = sigma*eta + sigma - b*row + alfa*row - alfa*mu*eta + b*mu*eta - alfa*delta - \
        alfa*delta*eta + alfa*beta*delta*eta + b*delta  # y
    E = sigma*eta - alfa*delta*eta + b*delta*eta

    return A, B, C, D, E


b_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.35]

eq_coef_lists = [[1.0175919999999998e-05, -0.0073482546552, 1.2707037438488, -8.700942237576001, -9.979004412],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2710147438488, -8.770333147576, -9.223292712],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2713257438488, -8.839724057576001, -8.467581012],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2716367438488003, -8.909114967576, -7.711869312],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2719477438488003, -8.978505877576, -6.956157612],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2722587438488002, -9.047896787575999, -6.200445911999999],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2725697438488002, -9.117287697576002, -5.444734212],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2728807438488001, -9.186678607576, -4.689022511999999],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2731917438488, -9.256069517576, -3.9333108119999993],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2735027438488, -9.325460427576001, -3.1775991119999993],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2738137438488, -9.394851337576, -2.4218874119999994],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2741247438488, -9.464242247576, -1.6661757119999994],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2744357438488003, -9.533633157575998, -0.9104640120000003],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2747467438488003, -9.603024067576, -0.1547523119999994],
                 [1.0175919999999998e-05, -0.0073482546552, 1.2749022438488002, -9.637719522576, 0.2231035380000037]]

y_lists = [[267.7979614607897, 8.189706664487801, 447.134228980832, -1],
           [267.83313853426284, 8.17000254110664, 447.0453175404535, -0.9265615097135083],
           [267.8683644420103, 8.149974254489223, 446.9563499858526, -0.8527915762427085],
           [267.90363930107105, 8.129611515662646, 446.8673261991779, -0.778679909802122],
           [267.93896322891294, 8.108903518210582, 446.778246062152, -0.7042157031660565],
           [267.97433634343236, 8.087838901712502, 446.6891094560706, -0.6293875951059533],
           [268.00975876296565, 8.066405711805373, 446.59991626179476, -0.5541836304562935],
           [268.0452306062786, 8.044591356494948, 446.51066635975656, -0.47859121642059677],
           [268.0807519925827, 8.022382558256623, 446.42135962994826, -0.40259707467808425],
           [268.11632304152596, 7.99976530144329, 446.33199595192707, -0.3261871887868608],
           [268.15194387319826, 7.976724774408467, 446.2425752048109, -0.2493467463081913],
           [268.1876146081403, 7.953245305688341, 446.1530972672721, -0.17206007499123643],
           [268.2233353673337, 7.929310293489721, 446.0635620175425, -0.09431057225640416],
           [268.25910627221316, 7.90490212759039, 445.9739693334054, -0.01608062709948399],
           [268.277010567361, 7.892514811925054, 445.9291514151162, 0.023220311707234487]]

x_lists = []

for i in range(len(b_list)):
    x_lists.append([])
    for j in y_lists[i]:
        if j == -1:
            x_lists[i].append(None)
            continue
        x_lists[i].append((alfa + alfa*j - alfa*beta*j - alfa*beta*(j**2) - b_list[i])/(1+j))

for i in x_lists:
    print(i)

print(x_lists)

'''
b = 0
[0.17297680277471758, 1.6092032797937954, 0.7597650701002963, None]
[447.134228980832, 8.189706664487801, 267.7979614607897, -1]

b = 1.35
[0.17389920358057684, 1.4583626185687077, 0.7531841967827184, 0.31656006549197335]
[445.9291514151162, 7.892514811925054, 268.277010567361, 0.023220311707234487]

Point A
0.31552230830884315
0

'''

'''
b = 0
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2707037438488 y**2
-8.700942237576001 y
-9.979004412

x1
267.7979614607897
x2
8.189706664487801
x3
447.134228980832
x4
-1

b = 0.1
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2710147438488 y**2
-8.770333147576 y
-9.223292712

x1
267.83313853426284
x2
8.17000254110664
x3
447.0453175404535
x4
-0.9265615097135083

b = 0.2
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2713257438488 y**2
-8.839724057576001 y
-8.467581012

x1
267.8683644420103
x2
8.149974254489223
x3
446.9563499858526
x4
-0.8527915762427085

b = 0.3
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2716367438488003 y**2
-8.909114967576 y
-7.711869312

x1
267.90363930107105
x2
8.129611515662646
x3
446.8673261991779
x4
-0.778679909802122

b = 0.4
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2719477438488003 y**2
-8.978505877576 y
-6.956157612

x1
267.93896322891294
x2
8.108903518210582
x3
446.778246062152
x4
-0.7042157031660565

b = 0.5
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2722587438488002 y**2
-9.047896787575999 y
-6.200445911999999

x1
267.97433634343236
x2
8.087838901712502
x3
446.6891094560706
x4
-0.6293875951059533

b = 0.6
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2725697438488002 y**2
-9.117287697576002 y
-5.444734212

x1
268.00975876296565
x2
8.066405711805373
x3
446.59991626179476
x4
-0.5541836304562935

b = 0.7
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2728807438488001 y**2
-9.186678607576 y
-4.689022511999999

x1
268.0452306062786
x2
8.044591356494948
x3
446.51066635975656
x4
-0.47859121642059677

b = 0.8
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2731917438488 y**2
-9.256069517576 y
-3.9333108119999993

x1
268.0807519925827
x2
8.022382558256623
x3
446.42135962994826
x4
-0.40259707467808425

b = 0.9
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2735027438488 y**2
-9.325460427576001 y
-3.1775991119999993

x1
268.11632304152596
x2
7.99976530144329
x3
446.33199595192707
x4
-0.3261871887868608

b = 1.0
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2738137438488 y**2
-9.394851337576 y
-2.4218874119999994

x1
268.15194387319826
x2
7.976724774408467
x3
446.2425752048109
x4
-0.2493467463081913

b = 1.1
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2741247438488 y**2
-9.464242247576 y
-1.6661757119999994

x1
268.1876146081403
x2
7.953245305688341
x3
446.1530972672721
x4
-0.17206007499123643

b = 1.2
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2744357438488003 y**2
-9.533633157575998 y
-0.9104640120000003

x1
268.2233353673337
x2
7.929310293489721
x3
446.0635620175425
x4
-0.09431057225640416

b = 1.3
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2747467438488003 y**2
-9.603024067576 y
-0.1547523119999994

x1
268.25910627221316
x2
7.90490212759039
x3
445.9739693334054
x4
-0.01608062709948399

b = 1.35
1.0175919999999998e-05 y**4
-0.0073482546552 y**3
1.2749022438488002 y**2
-9.637719522576 y
0.2231035380000037

x1
268.277010567361
x2
7.892514811925054
x3
445.9291514151162
x4
0.023220311707234487

 b = 0
[0.17297680277471758, 1.6092032797937954, 0.7597650701002963, None]
[447.134228980832, 8.189706664487801, 267.7979614607897, -1]

 b = 1.35
[0.17389920358057684, 1.4583626185687077, 0.7531841967827184, 0.31656006549197335]
[445.9291514151162, 7.892514811925054, 268.277010567361, 0.023220311707234487]

Point A
0.31552230830884315
0

'''

"""
b = 0
    x_list = []
    y_list = []
    y = 447.134228980832  # y1
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = 8.189706664487801  #y2
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = 267.7979614607897  #y3
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = -1  #y4
    y_list.append(y)
    x_list.append(None)

    print('\n', 'b = 0')
    print(x_list)
    print(y_list)

    b = 1.35
    x_list = []
    y_list = []
    y = 445.9291514151162  # y1
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = 7.892514811925054  # y2
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = 268.277010567361  # y3
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)
    y = 0.023220311707234487  # y4
    y_list.append(y)
    x = (alfa + alfa * y - alfa * beta * y - alfa * beta * y ** 2 - b) / (1 + y)
    x_list.append(x)

    print('\n', 'b = 1.35')
    print(x_list)
    print(y_list)

    print()
    print('Point A')
    print(sigma/delta)
    print(0)
"""

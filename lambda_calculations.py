"""Старые вычисления коэффициентов lambda"""
import main_functions

sigma = 0.1181
row = 1.131
eta = 20.19
delta = 0.3743
alfa = 1.636
beta = 0.002
mu = 0.00311

x1 = 0.1729768027747205
x2 = 1.609203279793796
x3 = 0.7597650701002939
x4 = 0.31552230830884315

y1 = 447.13422898083115
y2 = 8.189706664487744
y3 = 267.79796146079036
y4 = 0

x_list = [x1, x2, x3, x4]
y_list = [y1, y2, y3, y4]

fx_list = []
fy_list = []
gx_list = []
gy_list = []

for i in range(4):
    x = x_list[i]
    y = y_list[i]
    fx_list.append((row * y)/(eta + y) - mu * y - delta)
    fy_list.append((row * eta * x)/((eta + y)**2) - mu * x)
    gx_list.append(-y)
    gy_list.append(alfa - 2 * alfa * beta * y - x)

print(fx_list)
print(fy_list)
print(gx_list)
print(gy_list)
print()

p_list = []
q_list = []

for i in range(4):
    x = x_list[i]
    y = y_list[i]
    p_list.append(fx_list[i] * -1 + gy_list[i] * -1)
    q_list.append(fx_list[i] * gy_list[i] - gx_list[i] * fy_list[i])

lambdas = []
for i in range(4):
    lambdas.append(main_functions.roots_of_quadratic_equation(1, p_list[i], q_list[i]))

print()

print(p_list)
print(q_list)
print()

p_list = []
q_list = []

for i in range(4):
    x = x_list[i]
    y = y_list[i]
    p_list.append((row * y * -1)/(eta + y) + mu * y + delta - alfa + 2 * alfa * beta * y + x)
    q_list.append(((row * y * alfa)/(eta + y)) -
                  ((2 * row * y**2 * alfa * beta)/(eta + y)) -
                  ((row * y * x)/(eta + y)) -
                  (alfa * mu * y) +
                  (2 * alfa * beta * mu * y**2) +
                  (mu * x * y) -
                  (alfa * delta) +
                  (2 * alfa * beta * y * delta) +
                  (delta * x) +
                  (y * ((row * eta * x)/((eta + y)**2))) -
                  y * mu * x)

print(p_list)
print(q_list)

print()
for i in lambdas:
    print(i)
print()

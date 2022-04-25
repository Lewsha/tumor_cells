"""Старые вычисления коэффициентов lambda"""
import main_functions

sigma = 0.1181
row = 1.131
eta = 20.19
delta = 0.3743
alfa = 1.636
beta = 0.002
mu = 0.0027

b_list = [12]

y_lists = [[377.5720937657258, 367.90472625937474, 6.796219617079231+4.424536730688678j,
            6.796219617079231-4.424536730688678j, 0]]

x_lists = [[0.3688860516881936, 0.3996870117410943, (0.4495334313581578+0.6462502583209729j),
            (0.4495334313581578-0.6462502583209729j), 0.31552230830884315]]

fx_lists = []
fy_lists = []
gx_lists = []
gy_lists = []

for i in range(len(b_list)):
    fx_lists.append([])
    fy_lists.append([])
    gx_lists.append([])
    gy_lists.append([])
    for j in range(5):
        if x_lists[i][j] is None:
            fx_lists[i].append(None)
            fy_lists[i].append(None)
            gx_lists[i].append(None)
            gy_lists[i].append(None)
            continue

        fx_lists[i].append((row*y_lists[i][j])/(eta+y_lists[i][j]) - mu*y_lists[i][j] - delta)
        fy_lists[i].append((row*eta*x_lists[i][j])/((eta+y_lists[i][j])**2) - mu*x_lists[i][j])
        gx_lists[i].append(-1*y_lists[i][j])
        gy_lists[i].append(alfa - 2*alfa*beta*y_lists[i][j] - x_lists[i][j] - (b_list[i]/((1+y_lists[i][j])**2)))


p_lists = []
q_lists = []

for i in range(len(b_list)):
    p_lists.append([])
    q_lists.append([])
    for j in range(5):
        if fx_lists[i][j] is None:
            p_lists[i].append(None)
            q_lists[i].append(None)
            continue
        p_lists[i].append((-1)*fx_lists[i][j] + gy_lists[i][j]*(-1))
        q_lists[i].append(fx_lists[i][j]*gy_lists[i][j] - gx_lists[i][j]*fy_lists[i][j])

lambdas = []
for i in range(len(b_list)):
    lambdas.append([])
    for j in range(5):
        if p_lists[i][j] is None:
            lambdas[i].append((None, None))
            continue
        lambdas[i].append(main_functions.roots_of_quadratic_equation(1, p_lists[i][j], q_lists[i][j]))

print()

for i in range(len(b_list)):
    print(f'b = {b_list[i]}')
    for j in range(5):
        print(f'{x_lists[i][j]}, {y_lists[i][j]}: {lambdas[i][j]}')
    print()

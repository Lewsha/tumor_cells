"""Построение фазового портрета (набор кривых, исходящих из разных точек плоскости)"""
# Импортируем один из пакетов Matplotlib
import pylab
import main_functions
from separatrix import separatrix
from resting_points_calculation import resting_points_calc


def grid_build(mu=0.00311):
    """Функция для построения "сетки" из набора кривых, исходящих из разных точек"""

    new_x = 0.1
    new_y = 1
    grid = [(new_x, new_y)]

    x_lists = []
    y_lists = []

    points = resting_points_calc(mu=mu)
    print(points)

    if 0.0027 <= mu <= 0.013:
        for i in range(3):
            points[i] = list(points[i])
            for j in range(2):
                points[i][j] = float(points[i][j])

        pylab.scatter([points[0][0], points[1][0]],
                      [points[0][1], points[1][1]], s=50, zorder=2, color='black')
        pylab.scatter(points[2][0], points[2][1], s=50, zorder=2, edgecolors='black', color='w')
        pylab.annotate('B', xy=(points[0][0], points[0][1]), xytext=(points[0][0] + 0.1, points[0][1] - 30),
                       fontsize=30)
        pylab.annotate('G', xy=(points[1][0], points[1][1]), xytext=(points[1][0] + 0.1, points[1][1] - 2), fontsize=30)
        pylab.annotate('S', xy=(points[2][0], points[2][1]), xytext=(points[2][0] + 0.1, points[2][1] - 30),
                       fontsize=30)

        result = separatrix(mu=mu)
        pylab.plot(*result, zorder=1, color='red', linewidth=3, linestyle='dashed')

    for i in range(3):
        new_x = 0
        for j in range(2):
            grid.append([new_x, new_y])
            new_x += 1.2
        new_y += 200
    # grid.append([1.2, 500])
    grid.append([points[2][0] - 0.03, points[2][1]])
    grid.append([points[2][0] + 0.03, points[2][1]])
    grid.append([2.5, 600])
    grid.append([0.5, 1])

    for point_number in range(len(grid)):
        print(point_number)
        result = main_functions.runge_cutt(grid[point_number], mu=mu)
        x_lists.append(result[0])
        y_lists.append(result[1])

    result = []
    for x, y in zip(x_lists, y_lists):
        result.append(x)
        result.append(y)

    # Нарисуем двумерный график
    pylab.plot(*result, zorder=1)
    pylab.tick_params(axis='both', which='major', labelsize=20)
    pylab.yscale('log')
    # pylab.xlim(-0.01, 2)
    # pylab.ylim(0.7, 550)

    # Покажем окно с нарисованным графиком
    pylab.show()


if __name__ == "__main__":
    grid_build(mu=0.0027)

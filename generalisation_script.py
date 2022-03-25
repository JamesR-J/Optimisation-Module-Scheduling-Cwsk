import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import itertools

len_day = 8
full_time = 8
part_time = 4
full_time_wage = 12
part_time_wage = 7.5
constraints = [6, 5, 7, 8, 8, 7, 5, 6, 4]


def generaliser(len_day, full, part, full_wage, part_wage, constraint):
    x_n = 0
    y_n = 0

    if len_day < full:
        raise EOFError

    x_n += int(len_day / full) + (len_day - full)
    x_n -= int(len_day / full) - 1

    y_n += int(len_day / part) + (len_day - part)
    y_n -= int(len_day / part) - 1

    line_1 = []
    line_2 = []

    for i in range(x_n):
        line_1.append([(i + 1, i), (i + 1, i + int(full / 2))])
        line_1.append([(i + 1, i + int(full / 2) + 1), (i + 1, i + full)])
    lc1 = mc.LineCollection(line_1, linewidths=10)

    for i in range(int(y_n)):
        line_2.append([(i + 1, i), (i + 1, i + part)])
    lc2 = mc.LineCollection(line_2, linewidths=10)

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [x_n, y_n]})
    plt.yticks(np.arange(0, len_day + 1, 1))
    ax1.add_collection(lc1)
    ax2.add_collection(lc2)
    ax1.autoscale()
    ax2.autoscale()
    ax1.margins(0.1)
    ax2.margins(0.1)
    ax1.set_title('Full Time')
    ax2.set_title('Part Time')
    ax1.grid(axis='y')
    ax2.grid(axis='y')
    ax1.set_xlabel('x')
    ax2.set_xlabel('y')
    ax1.set_ylabel('Hours of the Day')
    labels1 = np.arange(1, x_n+1, 1)
    labels2 = np.arange(1, y_n+1, 1)
    ax1.set_xticks(labels1)
    ax2.set_xticks(labels2)
    plt.savefig('generalisation_graph.png', dpi = 1200)
    plt.show()

    x_val = np.zeros(((int(x_n) + int(y_n)), len(constraint)))

    for i in range(int(x_n)):
        j = i
        while j < int(full / 2) + i:
            x_val[i][j] += 1
            j += 1
        k = int(full / 2) + i + 1
        while k < full + i:
            x_val[i][k] += 1
            k += 1

    for i in range(int(y_n)):
        m = i
        while m < part + i:
            x_val[i + int(x_n)][m] += 1
            m += 1

    x_val[0][len(constraint) - 1] += 1
    x_val[1][len(constraint) - 1] += 1

    x_val = list(itertools.chain.from_iterable(x_val))
    x_val = ''.join(str(x_val).split(','))

    constraints = ''.join(str(constraint).split(','))

    profits = [full * full_wage] * int(x_n) + [part * part_wage] * int(y_n)
    profits = ''.join(str(profits).split(','))

    no_of_x = int(x_n)

    with open('staff_scheduling_data.txt', 'w') as f:
        f.write(
            '! Data file for Generalised_Staff_Scheduling.mos\nconstraints : ' + constraints + '\nprofits : ' + profits
                + '\nno_of_x : ' + str(
                    no_of_x) + '\nx_val : ' + x_val)

    return int(x_n), int(y_n)


x, y = generaliser(len_day, full_time, part_time, full_time_wage, part_time_wage, constraints)

print(str(x) + ' Full Timers Needed that work ' + str(full_time) + ' hours and ' + str(
    y) + ' Part Timers Needed that work ' + str(part_time) + ' hours for an ' + str(
    len_day) + ' hour day, with a ' + str(len(constraints)) + ' constraint and ' + str(
    x + y) + ' coefficient Linear Programming problem')

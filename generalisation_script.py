import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

len_day = 8
full_time = 7
part_time = 4


def generaliser(len_day, full, part):
    x_n = 0
    y_n = 0

    if len_day < full:
        raise EOFError

    x_n += int(len_day / full) + (len_day - full)
    x_n -= int(len_day/full)-1

    y_n += int(len_day / part) + (len_day - part)
    y_n -= int(len_day / part) - 1

    # x_n += len_day / full
    # x_n += (((len_day / full) - 1) * (full - 1))

    # y_n += len_day / part
    # y_n += (((len_day / part) - 1) * (part - 1))



    line_1 = []
    line_2 = []

    for i in range(x_n):
        line_1.append([(i + 1, i), (i + 1, i + int(full/2))])
        line_1.append([(i + 1, i + int(full/2) + 1), (i + 1, i + full)])
    lc1 = mc.LineCollection(line_1, linewidths=2)

    for i in range(int(y_n)):
        line_2.append([(i + 1, i), (i + 1, i + part)])
    lc2 = mc.LineCollection(line_2, linewidths=2)

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [x_n, int(y_n)]})
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
    plt.show()

    return int(x_n), int(y_n)


x, y = generaliser(len_day, full_time, part_time)

print(str(x) + ' Full Timers Needed that work ' + str(full_time) + ' hours and ' + str(
    y) + ' Part Timers Needed that work ' + str(part_time) + ' hours for an ' + str(len_day) + ' hour day')

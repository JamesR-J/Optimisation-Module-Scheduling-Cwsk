len_day = 8
full_time = 7
part_time = 4

def generaliser(len_day, full, part):
    x_n = 0
    y_n = 0

    if len_day < full_time:
        raise EOFError

    x_n += int(len_day / full) + (len_day-full)

    # x_n += len_day / full
    # x_n += (((len_day / full) - 1) * (full - 1))

    y_n += len_day / part
    y_n += (((len_day / part) - 1) * (part - 1))

    return int(x_n), int(y_n)

x, y = generaliser(len_day, full_time, part_time)

print(str(x) + ' Full Timers Needed that work ' + str(full_time) + ' hours and ' + str(y) + ' Part Timers Needed that work ' + str(part_time) + ' hours for an ' + str(len_day) + ' hour day')
import math
import random as rand

import numpy as num
import matplotlib.pyplot as plt
import time

numb_points = 1000

seed = time.time()
print(seed)
rand.seed(1611664462.5855956)

n_fig = 1


def load_data():
    data = num.loadtxt("./TwoDistributionsMixed.txt", delimiter=" ")
    full = [data[10000:], data[:10000]]
    values_x = []
    values_y = []
    ddaata = []

    for x in range(5000):
        values_x.append(full[1][0][x])
        values_y.append(full[1][1][x])

    for g in range(len(values_y)):
        ddaata.append([values_x[g], values_y[g]])

    plt.plot(values_x, values_y, 'x')
    plt.show()

    return ddaata


def run_new():
    global n_fig
    points = load_data()
    times = [10, 50, 100]
    alpha = 10 ** (-4)
    r1_and_r2 = [[[], [], [], []]] * 4

    for p in range(30):
        print(p)
        for y in times:
            r1 = rand.choice(points[:int(len(points) / 2)])
            r2 = rand.choice(points[int(len(points) / 2):])

            r1_ = []
            r2_ = []

            for t in range(y):
                for g in points:
                    distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
                    distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

                    if distance_r1_x < distance_r2_x:
                        r1[0] = (1 - alpha) * r1[0] + alpha * g[0]
                        r1[1] = (1 - alpha) * r1[1] + alpha * g[1]
                        r1_.append(r1[:])

                    if distance_r1_x > distance_r2_x:
                        r2[0] = (1 - alpha) * r2[0] + alpha * g[0]
                        r2[1] = (1 - alpha) * r2[1] + alpha * g[1]
                        r2_.append(r2[:])

            r1_and_r2[times.index(y)][0].append(r1[0])
            r1_and_r2[times.index(y)][1].append(r1[1])
            r1_and_r2[times.index(y)][2].append(r2[0])
            r1_and_r2[times.index(y)][3].append(r2[1])

            if p == 0:
                close_r1_x = []
                close_r1_y = []
                close_r2_x = []
                close_r2_y = []
                x_r1 = []
                y_r1 = []

                for g in points:
                    distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
                    distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

                    if distance_r1_x < distance_r2_x:
                        close_r1_x.append(g[0])
                        close_r1_y.append(g[1])

                    if distance_r1_x > distance_r2_x:
                        close_r2_x.append(g[0])
                        close_r2_y.append(g[1])
                for h in r1_:
                    x_r1.append(h[0])
                    y_r1.append(h[1])

                x_r2 = []
                y_r2 = []
                for h in r2_:
                    x_r2.append(h[0])
                    y_r2.append(h[1])

                plt.plot(close_r1_x, close_r1_y, 'x', color="red")
                plt.plot(close_r2_x, close_r2_y, 'x', color="blue")
                plt.plot(x_r1, y_r1, 'x', color="green")
                plt.plot(x_r2, y_r2, 'x', color="yellow")
                plt.axis('equal')
                plt.legend(['Figure ' + str(n_fig)])
                n_fig += 1
                plt.show()

    for gg in range(len(r1_and_r2) - 1):
        plot_normal(r1_and_r2[gg], times[gg])


def new_run_2():
    global n_fig
    points = load_data()
    times = [10, 50, 100]
    alpha = 10 ** (-4)

    r1_and_r2 = [[[], [], [], []]] * len(times)

    for p in range(30):
        for y in times:
            r1 = rand.choice(points[:int(len(points) / 2)])
            r2 = rand.choice(points[int(len(points) / 2):])

            r1_ = []
            r2_ = []

            d_x = 0
            d_y = 0
            d_x_2 = 0
            d_y_2 = 0

            for t in range(y):
                for g in points:
                    distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
                    distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

                    if distance_r1_x < distance_r2_x:
                        d_x += (g[0] - r1[0])
                        d_y += (g[1] - r1[1])

                    if distance_r1_x > distance_r2_x:
                        d_x_2 += (g[0] - r2[0])
                        d_y_2 += (g[1] - r2[1])

                r1[0] += (alpha / len(points)) * d_x
                r1[1] += (alpha / len(points)) * d_y
                r2[0] += (alpha / len(points)) * d_x_2
                r2[1] += (alpha / len(points)) * d_y_2
                r1_.append(r1)
                r2_.append(r2)

            r1_and_r2[times.index(y)][0].append(r1[0])
            r1_and_r2[times.index(y)][1].append(r1[1])
            r1_and_r2[times.index(y)][2].append(r2[0])
            r1_and_r2[times.index(y)][3].append(r2[1])

            if p == 0:
                close_r1_x = []
                close_r1_y = []
                close_r2_x = []
                close_r2_y = []
                x_r1 = []
                y_r1 = []

                for g in points:
                    distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
                    distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

                    if distance_r1_x < distance_r2_x:
                        close_r1_x.append(g[0])
                        close_r1_y.append(g[1])

                    if distance_r1_x > distance_r2_x:
                        close_r2_x.append(g[0])
                        close_r2_y.append(g[1])

                for h in r1_:
                    x_r1.append(h[0])
                    y_r1.append(h[1])

                x_r2 = []
                y_r2 = []

                for h in r2_:
                    x_r2.append(h[0])
                    y_r2.append(h[1])

                plt.plot(close_r1_x, close_r1_y, 'x', color="red")
                plt.plot(close_r2_x, close_r2_y, 'x', color="blue")
                plt.plot(x_r1, y_r1, 'x', color="green")
                plt.plot(x_r2, y_r2, 'x', color="yellow")
                plt.axis('equal')
                plt.legend(['Figure ' + str(n_fig)])
                n_fig += 1
                plt.show()

    for gg in range(len(r1_and_r2)):
        plot_normal(r1_and_r2[gg], times[gg])


def plot_normal(points, times):
    global n_fig
    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax0, ax1, ax2, ax3 = ax.flatten()
    ax0.boxplot(points[0], vert=True)
    ax0.set_title('Valores X de r1 para  ' + str(times))
    ax1.boxplot(points[1], vert=True)
    ax1.set_title('Valores Y de r1 para  ' + str(times))
    ax2.boxplot(points[2], vert=True)
    ax2.set_title('Valores X de r2 para  ' + str(times))
    ax3.boxplot(points[3], vert=True)
    ax3.set_title('Valores Y de r2 para  ' + str(times))
    fig.tight_layout()
    plt.legend(['Figure ' + str(n_fig)])
    n_fig += 1
    plt.show()


def average():
    global n_fig
    points = load_data()

    x_copy = []
    y_copy = []

    for x in points:
        x_copy.append(x[0])
        y_copy.append(x[1])

    while len(points) > 2:
        sample = points.pop()
        next_point = closest_point(points, sample)
        close = points.pop(next_point)

        points.append([(sample[0] + close[0]) / 2, (sample[1] + close[1]) / 2])

    plt.plot(x_copy, y_copy, 'x', color="blue")
    plt.plot(points[0][0], points[0][1], 'x', color="red")
    plt.plot(points[1][0], points[1][1], 'x', color="red")
    plt.axis('equal')
    plt.legend(['Figure ' + str(n_fig)])
    n_fig += 1
    plt.show()


def closest_point(dataset, point):
    closest = [[0, 0], 0]
    index = 0
    for x in dataset:
        distance = math.sqrt(((point[0] - x[0]) ** 2) + ((point[1] - x[1]) ** 2))
        dist = closest[1]
        if dist == 0 or distance < dist:
            closest.clear()
            closest = [x, distance]
    return dataset.index(closest[0])


def write_to_file(points_1, name):
    all_points = points_1
    open(str(name) + ".txt", 'w').close()
    f = open(str(name) + ".txt", "w")
    f.write(' '.join(map(str, all_points)))

    return all_points


def new_cluster(dataset):
    average_points = []
    passed_points = [[0, 0]]
    stop = False

    for x in dataset:
        close = closest_point(dataset, x)
        for xx in passed_points:
            cond = num.any(num.in1d(x, xx))
            if not cond:
                if len(passed_points) == 1:
                    passed_points.clear()
                passed_points.append(x)
                passed_points.append(close)
                new_x = num.average(x[0] + close[0])
                new_y = num.average(x[1] + close[1])
                average_points.append([new_x, new_y])

                if len(passed_points) >= len(dataset):
                    print("PASSEI")
                    stop = True
                    break

        if stop:
            break

    return average_points


# run_new()
# new_run_2()
average()

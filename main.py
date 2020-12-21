import math
import random as rand

import numpy as num
import matplotlib.pyplot as plt

numb_points = 1000


def load_data():
    data = num.loadtxt("./TwoDistributionsMixed.txt", delimiter=" ")
    full = [data[10000:], data[:10000]]
    values_x = []
    values_y = []
    ddaata = []

    for x in range(10000):
        values_x.append(full[1][0][x])
        values_y.append(full[1][1][x])

    for g in range(len(values_y)):
        ddaata.append([values_x[g], values_y[g]])

    return ddaata


def run():
    database = write_to_file(load_data(), "points")
    plot_begin(database)
    values_r = []
    close_r1 = []
    close_r2 = []
    for x in range(2):
        rand.seed(2)
        r1 = rand.choice(database)
        r2 = rand.choice(database)
        alpha = 10e-7
        for y in range(2):
            if y == 1:
                write_to_file([close_r1 + close_r2], "1st")
            for g in database:
                distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
                distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

                if distance_r1_x < distance_r2_x:
                    r1[0] = (1 - alpha) * r1[0] + alpha * g[0]
                    r1[1] = (1 - alpha) * r1[1] + alpha * g[1]
                    close_r1.append([r1[0], r1[1]])

                if distance_r1_x > distance_r2_x:
                    r2[0] = (1 - alpha) * r2[0] + alpha * g[0]
                    r2[1] = (1 - alpha) * r2[1] + alpha * g[1]
                    close_r2.append([r2[0], r2[1]])
    plot_rs(close_r1, close_r2)
    deviation = num.std([close_r1 + close_r2])
    print("VALOR DO DESVIO:  " + str(deviation))
    plot_normal(close_r1, close_r2)


def run_2():
    database = write_to_file(load_data(), "points")
    plot_begin(database)
    close_r1 = []
    close_r2 = []
    for x in range(30):
        r1 = rand.choice(database)
        r2 = rand.choice(database)
        alpha = 10e-7
        d_x = 0
        d_y = 0
        d_x_2 = 0
        d_y_2 = 0

        for g in database:
            distance_r1_x = math.sqrt(((r1[0] - g[0]) ** 2) + ((r1[1] - g[1]) ** 2))
            distance_r2_x = math.sqrt(((r2[0] - g[0]) ** 2) + ((r2[1] - g[1]) ** 2))

            if distance_r1_x < distance_r2_x:
                d_x += (g[0] - r1[0])
                d_y += (g[1] - r1[1])

            if distance_r1_x > distance_r2_x:
                d_x_2 += (g[0] - r2[0])
                d_y_2 += (g[1] - r2[1])

        r1[0] = (alpha / len(database)) * d_x
        r1[1] = (alpha / len(database)) * d_y
        r2[0] = (alpha / len(database)) * d_x_2
        r2[1] = (alpha / len(database)) * d_y_2
        close_r1.append(r1)
        close_r2.append(r2)

    plot_rs(close_r1, close_r2)


def plot_close(points_r1, points_r2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_s_r1 = []
    y_s_r1 = []
    x_s_r2 = []
    y_s_r2 = []
    for x in points_r1:
        x_s_r1.append(x[0])
        y_s_r1.append(x[1])

    for x in points_r2:
        x_s_r2.append(x[0])
        y_s_r2.append(x[1])

    ax.scatter(x_s_r1, y_s_r1, color='b', label="close to r1")
    ax.scatter(x_s_r2, y_s_r2, color='r', label="close to r2")
    ax.legend()

    plt.xlim(-15, 10)
    plt.ylim(-10, 10)
    plt.show()


def plot_normal(points, points2):
    x_r1 = []
    y_r1 = []
    x_r2 = []
    y_r2 = []
    for x in points:
        x_r1.append(x[0])
        y_r1.append(x[1])

    for x in points2:
        x_r2.append(x[0])
        y_r2.append(x[1])

    fig, ax = plt.subplots(nrows=2, ncols=2)
    ax0, ax1, ax2, ax3 = ax.flatten()
    ax0.hist(x_r1)
    ax0.set_title('Valores X de r1')
    ax1.hist(y_r1)
    ax1.set_title('Valores Y de r1')
    ax2.hist(x_r2)
    ax2.set_title('Valores X de r2')
    ax3.hist(y_r2)
    ax3.set_title('Valores Y de r2')
    fig.tight_layout()
    plt.show()


def plot_rs(points, points2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_r1, y_r1 = zip(*points)
    x_r2, y_r2 = zip(*points2)

    ax.scatter(x_r1, y_r1, color='b', label="r1")
    ax.scatter(x_r2, y_r2, color='r', label="r2")
    plt.xlim(-15, 10)
    plt.ylim(-10, 10)
    ax.legend()
    plt.show()


def plot_begin(points_r1):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_s_r1 = []
    y_s_r1 = []
    for x in points_r1:
        x_s_r1.append(x[0])
        y_s_r1.append(x[1])
    ax.scatter(x_s_r1, y_s_r1, label="dataset")
    ax.legend()
    plt.xlim(-15, 12)
    plt.ylim(-12, 7)
    plt.show()


def write_to_file(points_1, name):
    all_points = points_1
    open(str(name) + ".txt", 'w').close()
    f = open(str(name) + ".txt", "w")
    f.write(' '.join(map(str, all_points)))

    return all_points


def average_cluster(dataset):
    average = new_cluster(dataset)

    while len(average) > 2:
        average = new_cluster(average)
        print(average)

    plot_begin(average)


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


def closest_point(dataset, point):
    closest = [[0, 0], 0]
    for x in dataset:
        distance = math.sqrt(((point[0] - x[0]) ** 2) + ((point[1] - x[1]) ** 2))
        dist = closest[1]
        if dist == 0 or distance < dist:
            closest.clear()
            closest = [point, distance]
    return closest[0]


run()

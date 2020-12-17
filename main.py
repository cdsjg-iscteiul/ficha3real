import math
import random as rand
from itertools import cycle

import numpy as num
import matplotlib.pyplot as plt

numb_points = 1000
rand.seed(3)


def teste():
    points_set1 = []
    points_set2 = []
    values_r1_r2 = []

    mu_1 = (5, 5)
    mu_2 = (-3, -3)
    sigma_1 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 10), rand.randint(0, 5)))
    sigma_2 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 1), rand.randint(0, 5)))

    for t in range(numb_points):
        point_set1 = num.random.multivariate_normal(mu_1, sigma_1)
        point_set2 = num.random.multivariate_normal(mu_2, sigma_2)

        points_set1.append(point_set1)
        points_set2.append(point_set2)

    database = write_to_file(points_set1, points_set2, "points")
    plot_begin(database)
    for t in range(2):
        # r1 = rand.choice(database)
        # print("VALOR DO R1:   " + str(r1))
        # r2 = rand.choice(database)
        # print("VALOR DO R2:   " + str(r2))
        # alpha = 10e-7
        # test12 = changing(database, r1, r2, alpha)
        # test12 = new_change(database, r1, r2, alpha)
        # values_r1_r2.append(test12)
        # print("VALOR DOS R:   " + str(values_r1_r2))
        # if t == 1:
        # plotted = write_to_file(test12, [], "1st")

        average = new_cluster(database)

        while len(average) > 2:
            average = new_cluster(average)

        plot_begin(average)


# deviation = num.std(values_r1_r2)
# print(deviation)


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


def plot_rs(points):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print(str(points))
    r1 = points[0]
    r2 = points[1]

    ax.scatter(r1[0], r1[1], color='y', label="r1")
    ax.scatter(r2[0], r2[1], color='m', label="r2")
    ax.legend()

    plt.xlim(-15, 10)
    plt.ylim(-10, 10)
    plt.show()


def plot_begin(points_r1):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_s_r1 = []
    y_s_r1 = []
    for x in points_r1:
        x_s_r1.append(x[0])
        y_s_r1.append(x[1])
    ax.scatter(x_s_r1, y_s_r1, color='b', label="dataset")
    ax.legend()

    plt.xlim(-15, 10)
    plt.ylim(-10, 10)
    plt.show()


def write_to_file(points_1, points_2, name):
    all_points = points_1 + points_2

    f = open(str(name) + ".txt", "w")
    f.write(' '.join(map(str, all_points)))

    return all_points


def clustering(dataset):
    average_points = []
    running = True
    ciclo = cycle(dataset)
    prox = next(ciclo)
    while running:
        current, prox = prox, next(ciclo)
        new_x = num.average([current[0], prox[0]])
        new_y = num.average([current[1], prox[1]])
        average_points.append([new_x, new_y])
        if len(average_points) == len(dataset) // 2:
            running = False
    return average_points


def new_cluster(dataset):
    average_points = []
    copy = [[0, 0]]

    for x in dataset:
        close = closest_point(dataset, x)
        new_x = num.average([x[0], close[0]])
        new_y = num.average([x[1], close[1]])
        new_point = [new_x, new_y]
        copy.append(close)
        copy.append(x)
        average_points.append(new_point)
        list = num.where(dataset == x[0])

    print(len(copy))
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


def changing(dataset, r1, r2, alpha):
    result_data = [r1, r2]
    rand.seed()
    close_r1 = []
    close_r2 = []
    # print("VALOR ANTES RESULT:   " + str(result_data))
    x = 0
    while x < len(dataset):
        # print(x)
        t = dataset[x]
        distance_r1_x = math.sqrt(((r1[0] - t[0]) ** 2) + ((r1[1] - t[1]) ** 2))
        # distance_r1_x = math.hypot((r1[0] - t[0]), (r1[1] - t[1]))
        # print(distance_r1_x)
        distance_r2_x = math.sqrt(((r2[0] - t[0]) ** 2) + ((r2[1] - t[1]) ** 2))
        # distance_r2_x = math.hypot((r2[0] - t[0]), (r2[1] - t[1]))
        # print(distance_r2_x)

        if distance_r1_x < distance_r2_x:
            r1[0] = (1 - alpha) * r1[0] + alpha * t[0]
            r1[1] = (1 - alpha) * r1[1] + alpha * t[1]
            # print(r1)
            result_data[0] = r1
            # print("RESULT DATA:  " + str(result_data[0]))
            close_r1.append(t)

        if distance_r1_x > distance_r2_x:
            r2[0] = (1 - alpha) * r2[0] + alpha * t[0]
            r2[1] = (1 - alpha) * r2[1] + alpha * t[1]
            result_data[1] = r2
            close_r2.append(t)

        x += 1
    # print("VALOR DEPOIS RESULT:   " + str(result_data))
    plot_rs(result_data)
    plot_close(close_r1, close_r2)
    return result_data


def new_change(dataset, r1, r2, alpha):
    result_data = []
    d_x = 0
    d_y = 0
    d_x_2 = 0
    d_y_2 = 0
    close_r1 = []
    close_r2 = []
    for g in dataset:
        distance_r1_x = math.hypot((r1[0] - g[0]), (r1[1] - g[1]))
        distance_r2_x = math.hypot((r2[0] - g[0]), (r2[1] - g[1]))

        if distance_r1_x < distance_r2_x:
            d_x += (g[0] - r1[0])
            d_y += (g[1] - r1[1])
            close_r1.append(g)

        if distance_r1_x > distance_r2_x:
            d_x_2 += (g[0] - r2[0])
            d_y_2 += (g[1] - r2[1])
            close_r2.append(g)

        r1[0] = (alpha / len(dataset)) * d_x
        r1[1] = (alpha / len(dataset)) * d_y
        r2[0] = (alpha / len(dataset)) * d_x_2
        r2[1] = (alpha / len(dataset)) * d_y_2

    result_data.append(r1)
    result_data.append(r2)
    plot_close(close_r1, close_r2)

    # print(str(result_data))
    return result_data


def main_run():
    teste()


main_run()

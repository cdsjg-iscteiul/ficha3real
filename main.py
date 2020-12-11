import math
import random as rand
import numpy as num
import matplotlib.pyplot as plt

rand.seed(3)


def teste():
    points_set1 = []
    points_set2 = []

    mu_1 = (5, 5)
    mu_2 = (-3, -3)
    sigma_1 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 10), rand.randint(0, 5)))
    sigma_2 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 1), rand.randint(0, 5)))

    for t in range(100):
        point_set1 = num.random.multivariate_normal(mu_1, sigma_1)
        point_set2 = num.random.multivariate_normal(mu_2, sigma_2)

        points_set1.append(point_set1)
        points_set2.append(point_set2)

    database = write_to_file(points_set1, points_set2, "points")
    plot(database)

    for t in range(2):
        test12 = changing(database)
        if t == 1:
            plotted = write_to_file(test12, [], "1st")
            print(str(plotted))
            plot(plotted)


def plot(points):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = points[:, 0]
    y = points[:, 1]

    ax.scatter(x, y, color='r')
    plt.show()


def write_to_file(points_1, points_2, name):
    all_points = points_1 + points_2

    f = open(str(name) + ".txt", "w")
    f.write(' '.join(map(str, all_points)))

    return all_points


def changing(dataset):
    result_data = []
    r1 = rand.choice(dataset)
    r2 = rand.choice(dataset)
    alpha = 10e-7

    x = 0

    while x < len(dataset):
        # print(x)
        t = dataset[x]
        distance_r1_x = math.sqrt(((r1[0] - t[0]) ** 2) + ((r1[1] - t[1]) ** 2))
        # distance_r1_x = math.hypot((r1[0] - x[0]), (r1[1] - x[1]))
        # print(distance_r1_x)
        distance_r2_x = math.sqrt(((r2[0] - t[0]) ** 2) + ((r2[1] - t[1]) ** 2))
        # distance_r2_x = math.hypot((r2[0] - x[0]), (r2[1] - x[1]))
        # print(distance_r2_x)

        if distance_r1_x > distance_r2_x:
            r1 = (1 - alpha) * r1 + alpha * x
            result_data.append(r1)

        if distance_r2_x > distance_r1_x:
            r2 = (1 - alpha) * r2 + alpha * x
            result_data.append(r2)

        x += 1

    print("SAI DA CENA")
    return result_data


def main_run():
    teste()


main_run()

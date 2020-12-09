import math
import random as rand
import numpy as num
import matplotlib.pyplot as plt

rand.seed(3)


def teste():
    points_x = []
    points_y = []
    points_x_2 = []
    points_y_2 = []

    mu_1 = (5, 5)
    mu_2 = (-3, -3)
    print(rand.randint(0, 10))
    print(rand.randint(0, 10))
    sigma_1 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 10), rand.randint(0, 5)))
    sigma_2 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 1), rand.randint(0, 5)))

    for t in range(500):
        x = num.random.multivariate_normal(mu_1, sigma_1)
        y = num.random.multivariate_normal(mu_1, sigma_1)
        points_x.append(x)
        points_y.append(y)

    for b in range(500):
        x_2 = num.random.multivariate_normal(mu_2, sigma_2, tol=1e-6)
        y_2 = num.random.multivariate_normal(mu_2, sigma_2, tol=1e-6)
        points_x_2.append(x_2)
        points_y_2.append(y_2)

    database = write_to_file(points_x, points_y, points_x_2, points_y_2, "points")
    for t in range(10):
        teste12 = changing(database)
        if t == 1:
            write_to_file(teste12, [], [], [], "1st")


def plot(points1, points2, points3, points4):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(points1, points2, color="b", marker="s", label="1st set")
    ax.scatter(points3, points4, color="r", marker="o", label="2nd set")
    plt.legend(loc='upper left')
    plt.show()


def write_to_file(points_1, points_2, points_3, points_4, name):
    all_points = points_1 + points_2 + points_3 + points_4

    f = open(str(name) + ".txt", "w")
    f.write(' '.join(map(str, all_points)))

    return all_points


def changing(dataset):
    result_data = dataset
    r1 = rand.choice(result_data)
    r2 = rand.choice(result_data)
    alpha = 10e-7

    for x in dataset:
        # distance_r1_x = math.sqrt(((r1[0] - x[0]) ** 2) + ((r1[1] - x[1]) ** 2))
        distance_r1_x = math.hypot((r1[0] - x[0]), (r1[1] - x[1]))
        # distance_r2_x = math.sqrt(((r2[0] - x[0]) ** 2) + ((r2[1] - x[1]) ** 2))
        distance_r2_x = math.hypot((r2[0] - x[0]), (r2[1] - x[1]))

        if distance_r1_x > distance_r2_x:
            r1[0] = (1 - alpha) * r1[0] + alpha * x[0]
            r1[1] = (1 - alpha) * r1[1] + alpha * x[1]
            result_data.append(r1)

        elif distance_r2_x > distance_r1_x:
            r2[0] = (1 - alpha) * r2[0] + alpha * x[0]
            r2[1] = (1 - alpha) * r2[1] + alpha * x[1]
            result_data.append(r2)

    return result_data


def main_run():
    teste()


main_run()

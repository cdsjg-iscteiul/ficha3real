import random as rand
import numpy as num
import matplotlib.pyplot as plt


def teste():
    points_x = []
    points_y = []
    points_x_2 = []
    points_y_2 = []

    mu_1 = (5, 5)
    mu_2 = (-3, -3)
    sigma_1 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 10), rand.randint(0, 5)))
    sigma_2 = ((rand.randint(0, 10), rand.randint(0, 5)), (rand.randint(0, 1), rand.randint(0, 5)))

    for t in range(5000):
        x = num.random.multivariate_normal(mu_1, sigma_1)
        y = num.random.multivariate_normal(mu_1, sigma_1)
        points_x.append(x)
        points_y.append(y)

    for b in range(5000):
        x_2 = num.random.multivariate_normal(mu_2, sigma_2, tol=1e-6)
        y_2 = num.random.multivariate_normal(mu_2, sigma_2, tol=1e-6)
        points_x_2.append(x_2)
        points_y_2.append(y_2)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.scatter(points_x, points_y, color="b", marker="s", label="1")
    ax.scatter(points_x_2, points_y_2, color="r", marker="o", label="2")
    plt.legend(loc='upper left')
    plt.show()


def write_to_file(points_1, points_2, points_3, points_4):
    all_points = points_1 + points_2 + points_3 + points_4
    rand.shuffle(all_points)

    f = open("points.txt", "w")
    f.write(all_points)

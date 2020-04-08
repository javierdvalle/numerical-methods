import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_data(T, Y, overlap=False):
    d = len(Y[0])
    if overlap:
        for i in range(d):
            f = plt.plot(T, Y[:,i])
    else:
        fig, axs = plt.subplots(d)
        for i in range(d):
            f = axs[i].plot(T, Y[:,i])
    # plt.show()


def plot_2d(Y, title=''):
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    plt.scatter(Y[:,0], Y[:,1])


def plot_3d(Y, title=''):
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    ax = fig.gca(projection='3d')
    ax.plot(Y[:, 0], Y[:, 1], Y[:, 2])
    plt.draw()


def plot_3d_function(f, root, title=''):
    dim = len(root)
    assert dim == 2  # can only plot two-dimensional x
    n = 50
    x_axis_range = np.linspace(root[0]-7, root[0]+7, n)
    y_axis_range = np.linspace(root[1]-7, root[1]+7, n)
    for i in range(dim):
        xs = [j for j in x_axis_range for _ in x_axis_range]
        ys = list(y_axis_range) * len(y_axis_range)
        zs = [f([x, y])[i] for x, y in zip(xs, ys)]
        fig = plt.figure()
        ax = plt.gca(projection='3d')
        ax.scatter(xs, ys, zs, s=5)
        ax.scatter(root[0], root[1], f(root)[i], s=60, c='red')

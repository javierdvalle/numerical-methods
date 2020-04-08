import numpy as np
import scipy
import pylab as plt

from ..root_finding import newton_raphson


def plot_solution(f, root):
    x1 = np.linspace(-3,5,100)
    fig = plt.figure()
    plt.plot(x1, [f(a) for a in x1])
    plt.plot([root], [f(root)], color='r', marker='o')
    plt.grid()
    # plt.show()


if __name__ == '__main__':

    def f1(x):
        return (3.0-x)*scipy.exp(x) - 3.0

    def f2(x):
        return np.sin(x)

    def f3(x):
        return np.sin(x*2)/x

    root = newton_raphson(f1, x0=1, maxiter=50, show_progress=True)
    plot_solution(f1, root)

    root = newton_raphson(f2, x0=2, maxiter=50)
    plot_solution(f2, root)

    root = newton_raphson(f3, x0=2, maxiter=50)
    plot_solution(f3, root)

    plt.show()

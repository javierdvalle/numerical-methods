import numpy as np
import scipy
import pylab as plt
import itertools
from ..root_finding import newton_raphson_multi
from ..plots import plot_3d_function


if __name__ == '__main__':

    def my_f(x):
        return np.array([
            x[0] * x[1]-a[0],
            x[0] + x[1]-a[1]
        ])

    def my_f2(x):
        return np.array([
            x[0] * np.sin(x[0]) + 0.1,
            np.cos(x[0])*np.cos(x[1]) / (x[1] + 1)
        ])
     
    def my_f3(x):
        return np.array([
            np.sin(x[0]) / (x[0] + 0.5),
            np.cos(x[0])*np.cos(x[1]) / (x[1] + 1)
        ])

    f = my_f3
    x0 = [0.5, 0.5]

    root = newton_raphson_multi(f, x0, show_progress=True)

    print(f"Root found: x={root}, f(x)={f(root)}")

    plot_3d_function(f, root)
    plt.show()

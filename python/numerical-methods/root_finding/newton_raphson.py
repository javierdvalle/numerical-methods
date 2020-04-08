import numpy as np

from ..differentiation import secant_derivate
from ..differentiation import jacobian


def newton_raphson(f, x0, maxiter=50, tol=0.0001, show_progress=False):
    xn = x0
    i = 0
    a = tol+1
    while i < maxiter and np.abs(a) > tol:
        a = f(xn)/secant_derivate(f, xn)
        xn = xn - a
        i += 1
        if show_progress:
            print(f"i={i}, x={xn}")
    return xn


def newton_raphson_multi(f, x0, max_iter=50, tol=0.0001, show_progress=False):
    x1 = np.array(x0)
    e = 1.0
    i = 0
    while i < max_iter and e > tol:
        A = jacobian(f, x1)
        B = f(x1)
        res = np.linalg.solve(A, B)
        x1 = x1 - res
        e = max(abs(res.max()), abs(res.min()))
        if show_progress:
            print(f"{i} -> max abs error = {e}")
        i += 1
    return x1

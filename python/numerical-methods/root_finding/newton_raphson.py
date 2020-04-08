import numpy as np


def secant_derivate(f, x, h=0.001):
    return (f(x+h)-f(x))/h


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


def jacobian(f, x, a, tol=0.0001):
    res = []
    xtemp = np.array(x)
    x1 = xtemp.copy()
    for i in range(len(x1)):
        x2 = x1.copy()
        x2[i] += tol
        r = (f(x2,a) - f(x1,a)) / tol
        res.append(r)
    jac = np.array(res[0])
    for i in range(len(res)-1):
        jac = np.vstack((jac, np.array(res[i+1])))
    return jac.transpose()


def newton_raphson_multi(f, x0, a, max_iter=50, tol=0.0001, show_progress=False):
    x1 = np.array(x0)
    e = 1.0
    i = 0
    while i < max_iter and e > tol:
        A = jacobian(f, x1, a)
        B = f(x1, a)
        res = np.linalg.solve(A, B)
        x1 = x1 - res
        e = max(abs(res.max()), abs(res.min()))
        if show_progress:
            print(f"{i} -> max abs error = {e}")
        i += 1
    return x1

import numpy as np


def secant_derivate(f, x, h=0.001):
	return (f(x+h)-f(x))/h


def newton_raphson(f, x0, maxiter=50, tol=0.000001, show_progress=False):
	xn = x0
	i = 0
	a = tol+1
	while i < maxiter and np.abs(a) > tol:
		a = f(xn)/secant_derivate(f, xn)
		xn = xn - a
		i+=1
		if show_progress:
			print(f"i={i}, x={xn}")
	return xn

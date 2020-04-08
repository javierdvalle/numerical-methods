import numpy as np
import math

def method_order(method):
	""" 
	Experiment to determine the order of an ODE solver
	https://youtu.be/6O9D6am_RK4
	"""
	f = lambda t, y: np.array([1/(1+t)**2])
	exact = 0.5
	h = 0.1
	T,Y1 = method(f, t0 = 0, t_end = 1, y0 = [0], h = h)
	T,Y2 = method(f, t0 = 0, t_end = 1, y0 = [0], h = h/2)
	ratio = (Y1[-1][0] - exact) / (Y2[-1][0] - exact)
	p = round(math.log2(ratio))
	return p

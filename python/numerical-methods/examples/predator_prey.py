import numpy as np
import matplotlib.pyplot as plt

from ..utils import plot_data
from ..utils import plot_2d
from ..ode.euler import euler


if __name__ == '__main__':

	### Predator-prey (Lotka–Volterra equations)
	# https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
	###
	mu1 = 50  # prey
	mu2 = 25  # predator
	y0 = np.array([10, 10])
	f = lambda t, y: np.array([y[0] * (1 - y[1]/mu1),
							   -y[1] * (1 - y[0]/mu2)])	

	T,Y = euler(f, t0=0, t_end=50, y0=y0, h=0.01)

	plot_data(T, Y, overlap=True)
	plot_2d(Y, title='Predator-prey (Lotka–Volterra equations)')
	plt.show()

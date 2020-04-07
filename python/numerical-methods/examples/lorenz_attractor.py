import numpy as np
import matplotlib.pyplot as plt

from ..utils import plot_data
from ..utils import plot_3d
from ..ode.euler import euler


if __name__ == '__main__':

	### Lorenz attractor
	# https://en.wikipedia.org/wiki/Lorenz_system
	###
	alpha = 10
	betha = 8/3
	rho = 28
	f = lambda t, y: np.array([alpha * (y[1] - y[0]),
							   y[0] * (rho - y[2]) - y[1],
							   y[0]*y[1] - betha*y[2]])	

	T,Y = euler(f, t0=0, t_end=50, y0=[1,1,1], h=0.001)

	plot_data(T, Y, overlap=False)
	plot_3d(Y, title='Lorenz attractor')
	plt.show()

import numpy as np
import matplotlib.pyplot as plt

from ..utils import plot_data
from ..utils import plot_3d
from ..ode.euler import euler


if __name__ == '__main__':

	###
	# y'(t) = (sin(t), cos(t), exp(t))
	###
	f = lambda t, y: np.array([np.sin(t), np.cos(t), np.exp(t)])	

	T,Y = euler(f, t0=0, t_end=30, y0=np.array([0, 0, 0]), h=0.1)

	plot_data(T, Y, overlap=False)
	plot_3d(Y, title='y\'(t) = (sin(t), cos(t), exp(t))')
	plt.show()
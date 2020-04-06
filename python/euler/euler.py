import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euler(f, t0 = 0, t_end = 10, y0 = 0, h = 0.1):
	tn, yn = t0, y0
	T, Y = [], []
	d = len(y0)

	for _ in range(int((t_end-t0)/h)):
	    fn = f(tn, yn)
	    
	    assert len(fn) == d, "dimensions do not coincide"

	    yn = yn + h*fn

	    T.append(tn)
	    Y.append(yn)

	    tn = tn + h

	return T, np.array(Y)


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


if __name__ == '__main__':

	###
	# y'(t) = (sin(t), cos(t), exp(t))
	###
	f = lambda t, y: np.array([np.sin(t), np.cos(t), np.exp(t)])	

	T,Y = euler(f, t0=0, t_end=30, y0=np.array([0, 0, 0]), h=0.1)

	plot_data(T, Y, overlap=False)
	plot_3d(Y, title='y\'(t) = (sin(t), cos(t), exp(t))')
	plt.show()


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


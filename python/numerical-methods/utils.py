import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

from ..ode import euler
from ..ode import method_order


if __name__ == '__main__':
	assert method_order(euler) == 1

from sympy import *

from ..ode.symbolic import taylor
from ..ode.symbolic import method_order
from ..ode.symbolic import get_symbols


if __name__ == '__main__':

	t, h, y, y1 = get_symbols()

	t0 = 0
	y0 = 1

	def f(t, u):
		return sin(t-pi*u**2)

	# explicit Euler
	method = y0 + h*f(t0, y0)
	order = method_order(f, method, t0=t0, y0=y0)
	print(f"explicit euler - order: {order}")
	assert order == 1

	# implicit Euler
	method = y0 + h*f(t0+h, y1(h))
	order = method_order(f, method, t0=t0, y0=y0)
	print(f"implicit euler - order: {order}")
	assert order == 1

	# implicit mid point
	method = y0 + h*f( t0+(h/2), (y0+y1(h))/2)
	order = method_order(f, method, t0=t0, y0=y0)
	print(f"implicit mid point - order: {order}")
	assert order == 2

	# trapezoidal
	method = y0 + (h/2)*(f(t0, y0) + f(t0+h, y1(h)))
	order = method_order(f, method, t0=t0, y0=y0)
	print(f"trapezoidal - order: {order}")
	assert order == 2

	f = exp(t)
	print(f"f(t): {f}, taylor: {taylor(f,5,0)}")

	f = sin(t)
	print(f"f(t): {f}, taylor: {taylor(f,5,0)}")

	f = sin(t**2)
	print(f"f(t): {f}, taylor: {taylor(f,5,0)}")

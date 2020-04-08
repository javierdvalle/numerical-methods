
def secant_derivate(f, x, h=0.001):
    return (f(x+h)-f(x-h))/(2*h)


def partial_derivate(f, x, i, h):
    x_plus_h = x.copy()
    x_minus_h = x.copy()
    x_plus_h[i] += h
    x_minus_h[i] -= h
    return (f(x_plus_h)-f(x_minus_h))/(2*h)


def gradient(f, x, h=0.001):
    return [partial_derivate(f, x, i, h)
            for i in range(len(x))]


def component(f, i):
    return lambda *args: f(*args)[i]


def jacobian(f, x, h=0.001):
    n_components = len(f(x))
    return [gradient(component(f, j), x, h=h)
            for j in range(n_components)]

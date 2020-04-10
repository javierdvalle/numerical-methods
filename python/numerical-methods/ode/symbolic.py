from sympy import *

t = Symbol('t')
h = Symbol('h')
y = Function('y')
y1 = Function('y1')


def taylor(f, n, a):
    fnext = f
    taylor = 0
    for i in range(n+1):
        taylor += ( fnext.subs({t:a})/factorial(i) ) * (t - a)**(i)
        fnext = fnext.diff(t)
    return taylor


def method_order(f, method, t0, y0):
    exact = f(t, y(t))
    numerical = method

    replacements = [ (y1(h).diff(h,0).subs({h:0}), numerical.subs({h:0})) ]
    for i in range(1,10):
        exact_eval = exact.subs({t:t0}).subs({y(0):y0})
        numerical = numerical.diff(h)
        numerical_eval = numerical.subs({h:0})

        # reduce replacing already known terms
        for a in reversed(replacements):
            numerical_eval = numerical_eval.subs({a[0]: a[1]})

        # add term
        replacements.append( (y1(h).diff(h,i).subs({h:0}), numerical.subs({h:0})) )
        print(replacements)
        if numerical_eval != exact_eval:
            print("-->  ORDER:", i-1, "- LOCAL ERROR:", (1/factorial(i))*(exact_eval-numerical_eval))
            return i-1

        exact = exact.diff(t)
        exact = exact.subs({y(t).diff(t): f(t, y(t))})


def get_method(name, t0, y0):
    methods = {
        "explicit_euler": y0 + h*f(t0, y0),
        "implicit_euler": y0 + h*f(t0+h, y1(h)),
        "implicit_mid_point": y0 + h*f( t0+(h/2), (y0+y1(h))/2),
        "trapezoidal": y0 + (h/2)*(f(t0, y0) + f(t0+h, y1(h)))
    }
    return methods[name]


def get_symbols():
    return (t, h, y, y1)

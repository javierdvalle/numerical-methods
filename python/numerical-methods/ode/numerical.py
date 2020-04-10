import numpy as np
import math

def method_order(method, show_info=False, **kwargs):
    """ 
    Experiment to determine the order of an ODE solver
    https://youtu.be/6O9D6am_RK4
    """
    h = 0.1
    t_end = 1

    ## option 1
    f = lambda t, y: np.array([1/(1+t)**2])
    y = lambda t: np.array([-(1/(1+t))+1])
    exact = y(t_end)
    # exact = 0.5
    
    ## option 2
    # f = lambda t, y: np.array([np.exp(t)])
    # y = lambda t: np.array([np.exp(t)-1])
    # exact = y(t_end)
    # exact = 1.718281828459045
    
    T1,Y1 = method(f, t0 = 0, t_end = t_end, y0 = [0], h = h, **kwargs)
    T2,Y2 = method(f, t0 = 0, t_end = t_end, y0 = [0], h = h/2, **kwargs)
    ratio = (Y1[-1][0] - exact) / (Y2[-1][0] - exact)
    
    if show_info:
        print(f"exact={exact}, steps={(len(T1),len(T2))}, e1={(Y1[-1][0] - exact)}, e2={(Y2[-1][0] - exact)}")
    
    p = round(math.log2(ratio))

    if show_info:
        print(f"ratio={ratio}, log(ratio)={math.log2(ratio)}, orden={p}")
    
    return p

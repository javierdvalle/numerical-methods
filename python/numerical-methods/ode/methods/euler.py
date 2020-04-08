import numpy as np

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

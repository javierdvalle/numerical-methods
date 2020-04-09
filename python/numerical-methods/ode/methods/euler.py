import numpy as np

def euler(f, t0=0, t_end=10, y0=0, h=0.1):
    tn, yn = t0, y0
    ts, ys = [t0], [t0]

    assert len(f(t0, y0)) == len(y0)

    for _ in range(int((t_end-t0)/h)):
        yn = yn + h*f(tn, yn)
        tn = tn + h
        ts.append(tn)
        ys.append(yn)

    return ts, np.array(ys)

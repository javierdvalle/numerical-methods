import numpy as np

from .rungekutta_tables import RKclassic


def rungekutta_unidim(f, t0, t_end, y0, h, table):
    if table is None:
        table = RKclassic()
    tn, yn = t0, y0
    ts, ys = [], []
    c, A, b = table 
    s = len(c)   # number of ki

    for _ in range(int((t_end-t0)/h)):
        k = np.zeros(s)
        
        for i in range(s):
            k[i] = f(tn + c[i]*h, yn + h*np.dot(A[i,:i], k[:i]))
        
        yn = yn + h * np.dot(b, k)
        tn = tn + h
        
        ys.append(yn)
        ts.append(tn)
        
    return ts, ys


def rungekutta(f, t0, t_end, y0, h=0.001, table=None):
    if table is None:
        table = table_RK4()
    tn, yn = t0, y0
    ts, ys = [], []
    c, A, b = table
    s = len(c)   # number of ki
    d = len(y0)  # vectors dimmension
    for _ in range(int((t_end-t0)/h)):
        k = np.zeros((d,s))
        
        for i in range(s):
            ki = f(tn + c[i]*h, yn + h * np.sum(A[i,:i]*k[:,:i]))
            k[:,i] = ki.reshape(1,d)
        
        yn = yn + h * np.sum(b*k, axis=1)
        tn = tn + h
        
        ys.append(yn)
        ts.append(tn)
        
    return ts, np.array(ys)

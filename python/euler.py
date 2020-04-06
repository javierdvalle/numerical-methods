import math
import matplotlib.pyplot as plt

f = lambda t, y: math.sin(t)

t0, y0 = 0, 0
tn, yn = t0, y0
t_last = 10
h = 0.1
T, Y = [], []


def euler(tn, yn, h, f):
    return yn + h*f(tn, yn)


for i in range(int((t_last-t0)/h)):

    yn = euler(tn, yn, h, f)

    T.append(tn)
    Y.append(yn)

    tn = tn + h


plt.plot(Y)
plt.show()

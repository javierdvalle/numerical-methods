import math
import matplotlib.pyplot as plt

f = lambda t, y: math.sin(t)

t0, y0 = 0, 0
tn, yn = t0, y0
t_end = 15
h = 0.1
T, Y = [], []


for _ in range(int((t_end-t0)/h)):

    yn = yn + h*f(tn, yn)

    T.append(tn)
    Y.append(yn)

    tn = tn + h


plt.plot(Y)
plt.show()

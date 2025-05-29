import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def rk4_step(xn, hn, vn, f):
    xn1 = xn + hn
    k1 = f(xn, vn)
    k2 = f(xn + hn / 2, vn + (hn / 2) * k1)
    k3 = f(xn + hn / 2, vn + (hn / 2) * k2)
    k4 = f(xn + hn, vn + hn * k3)
    vn1 = vn + (hn / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return xn1, vn1

def rk4(x0, u0, h, rhs, n_max, x_max):

    dim = len(u0) if hasattr(u0, '__iter__') else 1
    if dim > 1:
        v = np.array([np.zeros(dim) for i in range(n_max)])
    else:
        v = np.zeros(n_max)
    x = np.zeros(n_max)

    v[0] = u0
    x[0] = x0

    steps = min(n_max - 1, int((x_max - x0) / h))
    for n in range(steps):

        x[n + 1], v[n + 1] = rk4_step(x[n], h, v[n], rhs)
        if (v[n + 1] > 4 * np.pi):
            v[n + 1] -= 8 * np.pi
    return x[:steps+1], v[:steps+1]

def rhs(y, t):
	return (1.05 - np.sin(y/5))

u = rk4(0, 0, 0.0001, rhs, 100000, 300)
            

plt.plot(u)
plt.legend(['φ(t), при φ(0) = 0'], loc = 2, fontsize=12)
plt.xlabel("t", fontsize=13)
plt.ylabel('${\\varphi}$',fontsize=13)
plt.grid(True)
plt.show()

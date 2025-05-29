import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D
from scipy.integrate import solve_ivp

def rhs(t, X):
    x, y = X
    return [y, x**5 - 5 * x**3 + 4 * x]

def smpl(t,x):
    return [-x**6 / 6 + 5 * x**4 / 4 - 2 * x**2 + 1, x]

def eq_quiver(rhs, limits, N=20):
    xlims, ylims = limits
    xs = np.linspace(xlims[0], xlims[1], N)
    ys = np.linspace(ylims[0], ylims[1], N)
    U = np.zeros((N, N))
    V = np.zeros((N, N))
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            vfield = rhs(0.0, [x, y])
            u, v = vfield
            U[i][j] = u / (u**2 + v**2)(1 / 2) / 2
            V[i][j] = v / (u**2 + v**2)(1 / 2) / 2
    return xs, ys, U, V

def plotonPlane(rhs, limits):
    plt.close()
    xlims, ylims = limits
    plt.xlim(xlims[0], xlims[1])
    plt.ylim(ylims[0], ylims[1])
    xs, ys, U, V = eq_quiver(rhs, limits)
    plt.quiver(xs, ys, U, V, alpha=0.8)

parametrs_closed = [(-1.7, 0.),(-0.5, 0.),(0.5, 0.),(1.7, 0.)]
parametrs_point = [(-2.4,3.),(2.4,-3.),(-2.5,3),(2.5,-3)]
parametrs_limit = [(-1.99,0.),(-0.01,0.),(0.01,0.),(1.99,0.),(-2.4575,3),(2.4575,-3)]

plt.xlabel('x', fontsize = 12)
plt.ylabel('U(x)', fontsize = 12)
plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
x = np.linspace(-3,3,1000)
y = - x**6 / 6 + (5 * x**4) / 4 - 2 * x**2 + 1
plt.figure(1)
plt.plot(x,y)
plt.show()

plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
for param in parametrs_closed:
    Sol = solve_ivp(rhs, [0., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'forestgreen')
    
for param in parametrs_point:
    Sol = solve_ivp(rhs, [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'red')
    
for param in parametrs_limit:
    Sol = solve_ivp(rhs, [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='forestgreen', lw=3),
                Line2D([0], [0], color='red', lw=3),
                Line2D([0], [0], color='gold', lw=3),
                Line2D([0], [0], color="r", lw=3)]

plt.show()

x = np.linspace(-3,3,1000)
y = - x**6 / 6 + (5 * x**4) / 4 - 2 * x**2 + 1
plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
for param in parametrs_closed:
    Sol = solve_ivp(rhs, [0., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'forestgreen')
    
for param in parametrs_point:
    Sol = solve_ivp(rhs, [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'red')
    
for param in parametrs_limit:
    Sol = solve_ivp(rhs, [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")
plt.plot(x,y,"grey", linestyle='--')

custom_lines = [Line2D([0], [0], color='forestgreen', lw=3),
                Line2D([0], [0], color='red', lw=3),
                Line2D([0], [0], color='gold', lw=3),
                Line2D([0], [0], color="r", lw=3),
                Line2D([0], [0], color="grey", lw=4)]
plt.show()

for param in parametrs_closed:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(rhs, [0., 20.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()
    
for param in parametrs_point:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    plt.xlim((0,1))
    plt.ylim((-3,3))
    Sol = solve_ivp(rhs, [0., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()
    
for param in parametrs_limit:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(rhs, [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()


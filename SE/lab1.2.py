import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D
from scipy.integrate import solve_ivp

def f1(alfa):
    def rhs(t, X):
        x, y = X
        return [y, -alfa * y + x**5 - 5 * x**3 + 4 * x]
    return rhs

def eq_quiver(f1, limits, N=20):
    xlims, ylims = limits
    xs = np.linspace(xlims[0], xlims[1], N)
    ys = np.linspace(ylims[0], ylims[1], N)
    U = np.zeros((N, N))
    V = np.zeros((N, N))
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            vfield = f1(alfa)(0.0, [x, y])
            u, v = vfield
            U[i][j] = u / (u**2 + v**2)(1 / 2) / 2
            V[i][j] = v / (u**2 + v**2)(1 / 2) / 2
    return xs, ys, U, V

def plotonPlane(f1, limits):
    plt.close()
    xlims, ylims = limits
    plt.xlim(xlims[0], xlims[1])
    plt.ylim(ylims[0], ylims[1])
    xs, ys, U, V = eq_quiver(f1(alfa), limits)
    plt.quiver(xs, ys, U, V, alpha=0.8)
    
alfa = 5.

parametrs_point = [(-2.,3.),(2.,-3.),(1.3,3.),(-1.3,-3.),(-1.,3.),(1.,-3.),(0.6,3.),(-0.6,-3.),(-0.3,3.),(0.3,-3),(-2.5,3.),(2.5,-3.)]
parametrs_limit = [(0.005,0.),(-0.005,0.),(-1.99,0.),(1.99,0.),(1.57,3.),(-1.57,-3.),(2.34,-3),(-2.34,3),(0.55,-3.),(-0.55,3.)]

plt.title("α = 5")
plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='b', lw=3),
                Line2D([0], [0], color='gold', lw=3)]
plt.show()

parametrs = [(-2.,3.),(2.,-3.)]
    
for param in parametrs:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()

alfa = -5.
parametrs_point = [(-0.99,0.),(0.99,0.),(1.01,0),(-1.01,0.),(-2.6,3.),(2.6,-3.),(-2.565,3.),(2.565,-3.),(-1.05,-0.1),(1.05,0.1),(0.874,-0.17),(0.874,-0.16),(-0.874,0.17),(-0.874,0.16),]
parametrs_limit = [(-2.,-3),(-2.57342,3.),(2.57342,-3.),(-1.9,-3.),(-1.02,-0.0443795),(1.02,0.0443795),(0.876,-0.16217717557),(-0.876,0.16217717557)]

plt.title("α = -5")

plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='b', lw=3),
                Line2D([0], [0], color='gold', lw=3)]

plt.show()
 
parametrs = [(-0.99,0.),(0.99,0.),(-2.6,3.),(2.6,-3.)]
    
for param in parametrs:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()

alfa = 4.
plt.title("α = 4")
parametrs_point = [(-2.5,3.),(2.5,-3.),(2.2,-3.),(-2.2,3.),(0.95,3.),(-0.95,-3.),(-1.7,-3.),(1.7,3.),(1.,-3.),(-1.,3.),(-0.3,3.),(0.3,-3.)]
parametrs_limit = [(-1.99,0.),(-0.01,0.),(0.01,0.),(1.99,0.),(-2.36,3),(2.36,-3.),(-1.5,-3.),(1.5,3.),(0.65,-3.),(-0.65,3.)]

plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='b', lw=3),
                Line2D([0], [0], color='gold', lw=3)]

plt.show()

parametrs = [(-2.5,3.),(2.5,-3.)]
    
for param in parametrs:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()

alfa = -4.
plt.title("α = -4")
parametrs_point = [(-2.55,3),(2.55,-3),(-1.,0.001),(1.,-0.001),(0.95,-0.0001),(-0.95,0.0001),(-2.6,3.),(2.6,-3.),(-1,0.1),(1,-0.1)]
parametrs_limit = [(-1.99,0.),(1.99,0.),(-2.5514,3),(2.5514,-3),(0.9528211719,-0.12),(-0.9528211719,0.12),(-0.99,-0.046),(0.99,0.046)]

plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='b', lw=3),
                Line2D([0], [0], color='gold', lw=3)]

plt.show()

parametrs = [(-2.55,3),(2.55,-3),(-1.,0.001),(-1.99,0.)]
    
for param in parametrs:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()

alfa = 0.
plt.title("α = 0")
parametrs_closed = [(-1.7, 0.),(-0.5, 0.),(0.5, 0.),(1.7, 0.)]
parametrs_point = [(-2.4,3.),(2.4,-3.),(-2.5,3),(2.5,-3)]
parametrs_limit = [(-1.99,0.),(-0.01,0.),(0.01,0.),(1.99,0.),(-2.4575,3),(2.4575,-3)]


plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
for param in parametrs_closed:
    Sol = solve_ivp(f1(alfa), [0., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'green')
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='green', lw=3),
                Line2D([0], [0], color='gold', lw=3),
                Line2D([0], [0], color="b", lw=3)]
plt.show()

for param in parametrs_closed:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [0., 20.], param, method = 'RK45', rtol=1e-12)
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
    Sol = solve_ivp(f1(alfa), [0., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()
    
for param in parametrs_limit:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()

alfa = 24**(1/2)

parametrs_point = [(-2.46,3.),(2.46,-3.),(-1.7,-3.),(1.7,3.),(-2.2,3.),(2.2,-3.),(1.4,3.),(-1.4,-3.),(-0.7,3.),(0.7,-3.),(-0.2,3.),(0.2,-3.)]
parametrs_limit = [(-2.341,3),(2.341,-3),(-1.55,-3),(1.55,3),(0.0001,0.),(-0.0001,0.),(0.55,-3),(-0.55,3.)]

plt.title("α = √24")
plt.xlim(-3., 3.)
plt.ylim(-3., 3.)
    
for param in parametrs_point:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'b')
    
for param in parametrs_limit:
    Sol = solve_ivp(f1(alfa), [-9., 9.], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    plt.plot(x1, y1, 'gold')
    
plt.scatter(-2,0,marker='x',c="r")
plt.scatter(0,0,marker='x',c="r")
plt.scatter(2,0,marker='x',c="r")
plt.scatter(-1,0,marker='o',c="b")
plt.scatter(1,0,marker='o',c="b")

custom_lines = [Line2D([0], [0], color='b', lw=3),
                Line2D([0], [0], color='gold', lw=3)]

parametrs = [(-2.46,3.),(2.46,-3.)]
    
for param in parametrs:
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('x(t)', fontsize = 12)
    Sol = solve_ivp(f1(alfa), [3.5, -14.5], param, method = 'RK45', rtol=1e-12)
    x1, y1 = Sol.y
    t = Sol.t
    plt.title("For point = {0}".format(param))
    plt.plot(t,x1)
    plt.show()
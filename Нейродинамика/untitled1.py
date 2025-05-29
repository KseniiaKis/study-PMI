
import numpy as np 
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
  
def rhs(y,t): 
    return g - np.sin(y/5)
  
g = 1.05
a = 2 * np.pi


Sol = solve_ivp(rhs, [0,80], [0], method = 'RK45',max_step = 0.05)

Sol.y = np.transpose(Sol.y[0])



for i in range(np.size(Sol.y)):
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
    if (Sol.y[i] > a):
        Sol.y[i] = Sol.y[i] - 2 * np.pi
 
    
plt.plot(Sol.t,Sol.y) 
 
plt.legend(['φ(t), при φ(0) = 0'], loc = 2, fontsize=12)
 # graphic
plt.xlabel("t", fontsize=13)
plt.ylabel('${\\varphi}$',fontsize=13)
plt.grid(True)
plt.show()
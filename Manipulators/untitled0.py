import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 4,3
from matplotlib.animation import FuncAnimation
a=0.12
b=0.1
def elips(phi):
    return np.array([0.75 + a * np.cos(phi), 0.5*(2**(1/2)+0.4) + b * np.sin(phi)])


fig, ax = plt.subplots()
ax.axis([-1.5,1.5,-1.5,1.5])
ax.set_aspect("equal")
point, = ax.plot(0,1, marker="o")

def update(phi):
    x,y = elips(phi)

    point.set_data([x],[y])
    return point,

ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                    frames=np.linspace(0,2*np.pi,360, endpoint=False))

t = np.linspace(0,360,360)

x = 0.75 + a*np.cos(np.radians(t))

y = 0.5*(2**(1/2)+0.4) + b*np.sin(np.radians(t))

plt.plot(x,y, color = "r")
plt.axvline (x=0.99,color = 'r', linestyle = '-')

plt.xlim([0, 1])
plt.ylim([-0.1, 1.1])

plt.show()
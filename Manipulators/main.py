import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x0 = 0
y0 = np.sqrt(2) / 4 + 0.4

l1 = 0.5
l2 = 0.5
l3 = 0.5

a1, a2, a3, a4 = 1, 1, 1, 1

r = 0.2

q0 = np.array([np.pi/4, np.pi/2, 0, 3*np.pi/4])

epsilon = 1e-5
po = 0.1

S = np.linspace(0,1,100)

delta_q = np.zeros(4)

deltaArr = [0]
iterArr = np.zeros((len(S)))

def x(t):
    return x0 - 3 * r * np.sin(2 * np.pi * t)

def y(t):
    return y0 + r * np.cos(2 * np.pi * t)

trajectory_x = [x(t) for t in S]
trajectory_y = [y(t) for t in S]

def c1(q):
    return l1 * np.cos(q[0]), l1 * np.sin(q[0])

def c2(q):
    return l1*np.cos(q[0])+(l2+q[2])*np.cos(q[1]), l1*np.sin(q[0])+(l2+q[2])*np.sin(q[1])

def c3(q):
    return l1*np.cos(q[0])+(l2+q[2])*np.cos(q[1])+l3*np.cos(q[3]), l1*np.sin(q[0])+(l2+q[2])*np.sin(q[1])+l3*np.sin(q[3])

def dFxdq1(q):
    return -l1 * np.sin(q[0])

def dFxdq2(q):
    return -(l2 + q[2])* np.sin(q[1])

def dFxdq3(q):
    return np.cos(q[1])

def dFxdq4(q):
    return -l3 * np.sin(q[3])

def dFydq1(q):
    return l1 * np.cos(q[0])

def dFydq2(q):
    return (l2 + q[2])* np.cos(q[1])

def dFydq3(q):
    return np.sin(q[1])

def dFydq4(q):
    return l3 * np.cos(q[3])

def buildMatrix(q):
    a11 = - (dFxdq1(q)) ** 2 / a1 - (dFxdq2(q)) ** 2 / a2 -  (dFxdq3(q)) ** 2 / a3 - (dFxdq4(q)) ** 2 / a4
    a12 = - (dFxdq1(q) * dFydq1(q)) / a1 - (dFxdq2(q) * dFydq2(q)) / a2 - (dFxdq3(q) * dFydq3(q)) / a3 - (dFxdq4(q) * dFydq4(q)) / a4
    a21 = a12
    a22 = - (dFydq1(q)) ** 2 / a1 - (dFydq2(q)) ** 2 / a2 - (dFydq3(q)) ** 2 / a3 - (dFydq4(q)) ** 2 / a4
    return np.array([[a11, a12], [a21, a22]])

def build_b(q, t):
    return np.array([x(t)- c3(q)[0], y(t)- c3(q)[1]])

    # for i in range(1, len(S)):
    #     q = q0
    #     counter = 0

def solve(q, t):
    while True:
        # counter += 1
        coefArr = buildMatrix(q)
        bArr = build_b(q, t)
        Mx, My = np.linalg.solve(coefArr, bArr)
        
        delta_q[0] = -1 / a1 * (Mx * dFxdq1(q) + My * dFydq1(q))
        delta_q[1] = -1 / a2 * (Mx * dFxdq2(q) + My * dFydq2(q))
        delta_q[2] = -1 / a3 * (Mx * dFxdq3(q) + My * dFydq3(q))
        delta_q[3] = -1 / a4 * (Mx * dFxdq4(q) + My * dFydq4(q))
        q = q + delta_q
        
        delta = max(abs(0.5*np.cos(q[0])+(0.5+q[2])*np.cos(q[1])+0.5*np.cos(q[3])-x(t)), abs(0.5*np.sin(q[0])+(0.5+q[2])*np.sin(q[1])+0.5*np.sin(q[3])-y(t)))
        if delta < epsilon:
            break
            
        if (0.75-(0.5*np.cos(q[0])+(0.5+q[2])*np.cos(q[1]))) > po:
            deltaArr.append(delta_q)
            #iterArr[t] = counter
        else:
                #counter = 0
                while True:
                    #counter += 1
                    securityZone = (-0.75+0.5*np.cos(q[0])+(0.5+q[2])*np.cos(q[1]))
                    coefArr = np.array([[- (dFxdq1(q)) ** 2 / a1 / 2 - (dFxdq2(q)) ** 2 / a2 -  (dFxdq3(q)) ** 2 / a3 - (dFxdq4(q)) ** 2 / a4, - (dFxdq1(q) * dFydq1(q)) / a1 / 2 - (dFxdq2(q) * dFydq2(q)) / a2 - (dFxdq3(q) * dFydq3(q)) / a3 - (dFxdq4(q) * dFydq4(q)) / a4, securityZone*((-1/a1)*0.5*np.sin(q[0])**2-(1/a2)*2*((0.5+q[2])**2)*np.sin(q[1])**2-(1/a3)*2*np.cos(q[1])**2)],
                                        [- (dFxdq1(q)) ** 2 / a1/ 2 - (dFxdq2(q)) ** 2 / a2 -  (dFxdq3(q)) ** 2 / a3 - (dFxdq4(q)) ** 2 / a4, - (dFydq1(q)) ** 2 / a1 / 2 - (dFydq2(q)) ** 2 / a2 - (dFydq3(q)) ** 2 / a3 - (dFydq4(q)) ** 2 / a4, securityZone*((1/a1)*0.5*np.sin(q[0])*np.cos(q[0])+(1/a2)*2*((0.5+q[2])**2)*np.sin(q[1])*np.cos(q[1])-(1/a3)*2*np.cos(q[1])*np.sin(q[1]))],
                                        [securityZone*((-1/a1)*0.5*np.sin(q[0])**2-(1/a2)*2*((0.5+q[2])**2)*np.sin(q[1])**2-(1/a3)*2*np.cos(q[1])**2), securityZone*((1/a1)*0.5*np.sin(q[0])*np.cos(q[0])+(1/a2)*2*((0.5+q[2])**2)*np.sin(q[1])*np.cos(q[1])-(1/a3)*2*np.cos(q[1])*np.sin(q[1])), (securityZone**2)*((-1/a1)*np.sin(q[0])**2-(1/a2)*4*((0.5+q[2])**2)*np.sin(q[1])**2-(1/a3)*4*np.cos(q[1])**2)]])
                    bArr = np.array([x(t) - 0.5 * np.cos(q[0]) - (0.5 + q[2]) * np.cos(q[1]) - 0.5 * np.cos(q[3]), y(t) - 0.5 * np.sin(q[0]) - (0.5 + q[2]) * np.sin(q[1]) - 0.5 * np.sin(q[3]), po**2-(0.5 * np.cos(q[0]) + (0.5 + q[2]) * np.cos(q[1]) - 0.75)**2])
                    Mx, My, Mr = np.linalg.solve(coefArr, bArr)
                    delta_q[0] = (-Mx * 0.5 * np.sin(q[0]) + My * 0.5 * np.cos(q[0])-Mr*securityZone*np.sin(q[0])) / (-a1)
                    delta_q[1] = (-Mx * (q[2] + 0.5) * np.sin(q[1]) + My * (q[2] + 0.5) * np.cos(q[1]) - Mr*securityZone*2*(q[2] + 0.5)*np.sin(q[1])) / (-a2)
                    delta_q[2] = (Mx * np.cos(q[1]) + My * np.sin(q[1]) + Mr*securityZone*2*np.cos(q[1])) / (-a3)
                    delta_q[3] = (-Mx * 0.5 * np.sin(q[3]) + My * 0.5 * np.cos(q[3])) / (-a4)
                    q = q + delta_q
                    delta = max(abs(0.5 * np.cos(q[0]) + (0.5 + q[2]) * np.cos(q[1]) + 0.5 * np.cos(q[3]) - x(t)), abs(0.5 * np.sin(q[0]) + (0.5 + q[2]) * np.sin(q[1]) + 0.5 * np.sin(q[3]) - y(t)))
                    if (delta < epsilon):
                        deltaArr.append(delta_q)
                        q = q
                        #iterArr[t] = counter
                        break
    return delta_q

def move(t, q):
    q_new = q.copy()
    for _ in range(1000):
        q_new += solve(q_new, t)
    return q_new

def start(tmax):
    t = 0
    q = [q0]
    while t <= tmax:
        q.append(move(t, q[-1]))
        t += 0.01
    return q

dots = start(100)

trajectory_x = [x(t) for t in np.linspace(0, 2 * np.pi, 300)]
trajectory_y = [y(t) for t in np.linspace(0, 2 * np.pi, 300)]

fig, ax = plt.subplots()
ax.set_xlim((-1, 2))
ax.set_ylim((-1, 2))

ax.axvline(x=0.75, color='gray')

ax.plot(trajectory_x, trajectory_y, 'b--', dashes=[5, 5])

link1, = ax.plot([], [], 'ko-')
link2, = ax.plot([], [], 'ko-')
link3, = ax.plot([], [], 'ko-')


def init():
    link1.set_data([], [])
    link2.set_data([], [])
    link3.set_data([], [])
    return link1, link2, link3


def update(frame):
    q1, q2, q3, q4 = dots[frame]
    x1, y1 = c1(q1, q2, q3, q4)
    x2, y2 = c2(q1, q2, q3, q4)
    x3, y3 = c3(q1, q2, q3, q4)

    link1.set_data([0, x1], [0, y1])
    link2.set_data([x1, x2], [y1, y2])
    link3.set_data([x2, x3], [y2, y3])

    return link1, link2, link3


ani = FuncAnimation(fig, update, frames=len(dots), init_func=init, blit=True, interval=100)

plt.show()
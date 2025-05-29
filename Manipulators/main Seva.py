import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l1 = 0.5
l2 = 0.25
l3 = 0.25
l4 = 0.5

a1 = 81
a2 = 27
a3 = 9
a4 = 3

x0 = 0
y0 = np.sqrt(2) / 4 + 0.4

r = 0.2

epsilon = 1e-5


def dFxdq1(q1, q2, q3, q4):
    return -l1 * np.sin(q1)


def dFxdq2(q1, q2, q3, q4):
    return -l2 * np.sin(q2) - (q3 + l3) * np.sin(q2)


def dFxdq3(q1, q2, q3, q4):
    return np.cos(q2)


def dFxdq4(q1, q2, q3, q4):
    return -l4 * np.sin(q4)


def dFydq1(q1, q2, q3, q4):
    return l1 * np.cos(q1)


def dFydq2(q1, q2, q3, q4):
    return l2 * np.cos(q2) + (q3 + l3) * np.cos(q2)


def dFydq3(q1, q2, q3, q4):
    return np.sin(q2)


def dFydq4(q1, q2, q3, q4):
    return l4 * np.cos(q4)


def buildMatrix(q1, q2, q3, q4):
    a11 = - (dFxdq1(q1, q2, q3, q4)) ** 2 / a1 - (dFxdq2(q1, q2, q3, q4)) ** 2 / a2 - \
          (dFxdq3(q1, q2, q3, q4)) ** 2 / a3 - (dFxdq4(q1, q2, q3, q4)) ** 2 / a4
    a12 = - (dFxdq1(q1, q2, q3, q4) * dFydq1(q1, q2, q3, q4)) / a1 - \
          (dFxdq2(q1, q2, q3, q4) * dFydq2(q1, q2, q3, q4)) / a2 - \
          (dFxdq3(q1, q2, q3, q4) * dFydq3(q1, q2, q3, q4)) / a3 - \
          (dFxdq4(q1, q2, q3, q4) * dFydq4(q1, q2, q3, q4)) / a4
    a21 = a12
    a22 = - (dFydq1(q1, q2, q3, q4)) ** 2 / a1 - (dFydq2(q1, q2, q3, q4)) ** 2 / a2 - \
          (dFydq3(q1, q2, q3, q4)) ** 2 / a3 - (dFydq4(q1, q2, q3, q4)) ** 2 / a4
    return np.array([[a11, a12], [a21, a22]])


def equal(q1, q2, q3, q4, new_x, new_y):
    x, y = calculate_4(q1, q2, q3, q4)
    return np.array([new_x - x, new_y - y])


def solve(q1, q2, q3, q4, new_x, new_y):
    A = buildMatrix(q1, q2, q3, q4)
    b = equal(q1, q2, q3, q4, new_x, new_y)
    x = np.linalg.solve(A, b)
    Mx, My = x
    dq1 = -1 / a1 * (Mx * dFxdq1(q1, q2, q3, q4) + My * dFydq1(q1, q2, q3, q4))
    dq2 = -1 / a2 * (Mx * dFxdq2(q1, q2, q3, q4) + My * dFydq2(q1, q2, q3, q4))
    dq3 = max(-1 / a3 * (Mx * dFxdq3(q1, q2, q3, q4) + My * dFydq3(q1, q2, q3, q4)), -q3)
    dq4 = -1 / a4 * (Mx * dFxdq4(q1, q2, q3, q4) + My * dFydq4(q1, q2, q3, q4))
    return np.array([dq1, dq2, dq3, dq4])

def x(t):
    return x0 - 3 * r * np.sin(2 * np.pi * t)

def y(t):
    return y0 + r * np.cos(2 * np.pi * t)

def calculate_1(q1, q2, q3, q4):
    return l1 * np.cos(q1), l1 * np.sin(q1)

def calculate_2(q1, q2, q3, q4):
    x1, y1 = calculate_1(q1, q2, q3, q4)
    return x1 + l2 * np.cos(q2), y1 + l2 * np.sin(q2)

def calculate_3(q1, q2, q3, q4):
    x2, y2 = calculate_2(q1, q2, q3, q4)
    return x2 + (q3 + l3) * np.cos(q2), y2 + (q3 + l3) * np.sin(q2)

def calculate_4(q1, q2, q3, q4):
    x3, y3 = calculate_3(q1, q2, q3, q4)
    return x3 + l4 * np.cos(q4), y3 + l4 * np.sin(q4)


def move(t, old_value):
    new_x = x(t + 0.01)
    new_y = y(t + 0.01)
    new_value = old_value.copy()
    for _ in range(1000):
        new_value += solve(*new_value, new_x, new_y)
        x1, y1 = calculate_1(*new_value)
        x2, y2 = calculate_2(*new_value)
        x3, y3 = calculate_3(*new_value)
        x4, y4 = calculate_4(*new_value)

        if x1 > 0.75 - 0.025 or x2 > 0.75 - 0.025 or x3 > 0.75 - 0.025 or x4 > 0.75 - 0.025:
            new_x = min(x1, x2, x3, x4, new_x) - 0.025

        if np.sqrt((x4 - new_x) ** 2 + (y4 - new_y) ** 2) < epsilon:
            break

    return new_value

def start(tmax):
    t = 0
    dots = [np.array([np.pi / 4, np.pi / 4, 0, np.pi / 4])]
    while t <= tmax:
        dots.append(move(t, dots[-1]))
        t += 0.01
    return dots

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
link4, = ax.plot([], [], 'ko-')


def init():
    link1.set_data([], [])
    link2.set_data([], [])
    link3.set_data([], [])
    link4.set_data([], [])
    return link1, link2, link3, link4


def update(frame):
    q1, q2, q3, q4 = dots[frame]
    x1, y1 = calculate_1(q1, q2, q3, q4)
    x2, y2 = calculate_2(q1, q2, q3, q4)
    x3, y3 = calculate_3(q1, q2, q3, q4)
    x4, y4 = calculate_4(q1, q2, q3, q4)

    link1.set_data([0, x1], [0, y1])
    link2.set_data([x1, x2], [y1, y2])
    link3.set_data([x2, x3], [y2, y3])
    link4.set_data([x3, x4], [y3, y4])

    return link1, link2, link3, link4


ani = FuncAnimation(fig, update, frames=len(dots), init_func=init, blit=True, interval=100)

plt.show()

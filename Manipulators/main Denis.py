import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import PillowWriter


if __name__ == '__main__':
    fig = plt.figure()
    backgroundTriangle, = plt.plot([], [], color='black')
    backgroundEllipse, = plt.plot([], [], '--')
    backgroundWall, = plt.plot([], [], color='red')
    backgroundForbiddenArea, = plt.plot([], [],  '--', color='red')
    animPlot, = plt.plot([], [], color='black', lw=2, marker='o')
    plt.xlim(-0.7, 0.8)
    plt.ylim(-0.1, 1.3)

    metadata = dict(title='RobotManipulator', artist='ErmolaevDenis')
    writer = PillowWriter(fps=24, metadata=metadata)

    S = np.linspace(0,1,100)
    Px = -0.6 * np.sin(2 * np.pi * S)
    Py = (0.5 * np.sqrt(2)/2 + 0.4) + (0.5 * np.sqrt(2)/2 + 0.1) * np.cos(2 * np.pi * S)

    with writer.saving(fig, "RobotManipulator.gif", 200):

        backgroundEllipse.set_data(Px, Py)
        backgroundTriangle.set_data([-0.1,  0.1,  0., -0.1], [-0.1,  -0.1,  0., -0.1])
        backgroundWall.set_data([0.75], [-0.1, 2])
        backgroundForbiddenArea.set_data([0.65], [-0.1, 2])

        q = np.array([np.pi/4, np.pi/2, 0, 3*np.pi/4])
        animPlot.set_data([0, 0.5*np.cos(q[0]), 0.5*np.cos(q[0])+(0.5+q[2])*np.cos(q[1]), 0.5*np.cos(q[0])+(0.5+q[2])*np.cos(q[1])+0.5*np.cos(q[3])],
                          [0, 0.5*np.sin(q[0]), 0.5*np.sin(q[0])+(0.5+q[2])*np.sin(q[1]), 0.5*np.sin(q[0])+(0.5+q[2])*np.sin(q[1])+0.5*np.sin(q[3])])
        writer.grab_frame()

        eps = 10**-5
        a1, a2, a3, a4 = 1, 1, 1, 1
        delta_q = np.zeros(4)
        po = 0.1
        deltaArr = np.zeros(len(S))
        iterArr = np.zeros((len(S)))
        for i in range(1, len(S)):
            q_internal = q
            counter = 0
            while True:
                counter += 1
                coefArr = np.array([[(-1/a1)*0.25*np.sin(q_internal[0])**2-(1/a2)*((q_internal[2]+0.5)**2)*np.sin(q_internal[1])**2-(1/a3)*np.cos(q_internal[1])**2-(1/a4)*0.25*np.sin(q_internal[3])**2,
                                     (1/a1)*0.25*np.sin(q_internal[0])*np.cos(q_internal[0])+(1/a2)*((q_internal[2]+0.5)**2)*np.sin(q_internal[1])*np.cos(q_internal[1])-(1/a3)*np.cos(q_internal[1])*np.sin(q_internal[1])+(1/a4)*0.25*np.sin(q_internal[3])*np.cos(q_internal[3])],
                                    [(1/a1)*0.25*np.sin(q_internal[0])*np.cos(q_internal[0])+(1/a2)*((q_internal[2]+0.5)**2)*np.sin(q_internal[1])*np.cos(q_internal[1])-(1/a3)*np.cos(q_internal[1])*np.sin(q_internal[1])+(1/a4)*0.25*np.sin(q_internal[3])*np.cos(q_internal[3]),
                                     (-1/a1)*0.25*np.cos(q_internal[0])**2-(1/a2)*((q_internal[2]+0.5)**2)*np.cos(q_internal[1])**2-(1/a3)*np.sin(q_internal[1])**2-(1/a4)*0.25*np.cos(q_internal[3])**2]])
                bArr = np.array([Px[i]-0.5*np.cos(q_internal[0])-(0.5+q_internal[2])*np.cos(q_internal[1])-0.5*np.cos(q_internal[3]),
                                 Py[i]-0.5*np.sin(q_internal[0])-(0.5+q_internal[2])*np.sin(q_internal[1])-0.5*np.sin(q_internal[3])])
                Mx, My = np.linalg.solve(coefArr, bArr)
                delta_q[0] = (-Mx * 0.5 * np.sin(q_internal[0]) + My * 0.5 * np.cos(q_internal[0])) / (-a1)
                delta_q[1] = (-Mx * (q_internal[2] + 0.5) * np.sin(q_internal[1]) + My * (q_internal[2] + 0.5) * np.cos(q_internal[1])) / (-a2)
                delta_q[2] = (Mx * np.cos(q_internal[1]) + My * np.sin(q_internal[1])) / (-a3)
                delta_q[3] = (-Mx * 0.5 * np.sin(q_internal[3]) + My * 0.5 * np.cos(q_internal[3])) / (-a4)
                q_internal = q_internal + delta_q
                delta = max(abs(0.5*np.cos(q_internal[0])+(0.5+q_internal[2])*np.cos(q_internal[1])+0.5*np.cos(q_internal[3])-Px[i]),
                            abs(0.5*np.sin(q_internal[0])+(0.5+q_internal[2])*np.sin(q_internal[1])+0.5*np.sin(q_internal[3])-Py[i]))
                if delta < eps:
                    break

            if (0.75-(0.5*np.cos(q_internal[0])+(0.5+q_internal[2])*np.cos(q_internal[1]))) > po:
                q = q_internal
                deltaArr[i] = delta
                iterArr[i] = counter
            else:
                q_internal = q
                counter = 0
                while True:
                    counter += 1
                    expression = (-0.75+0.5*np.cos(q_internal[0])+(0.5+q_internal[2])*np.cos(q_internal[1]))
                    coefArr = np.array([[(-1 / a1) * 0.25 * np.sin(q_internal[0]) ** 2 - (1 / a2) * (
                                (q_internal[2] + 0.5) ** 2) * np.sin(q_internal[1]) ** 2 - (1 / a3) * np.cos(
                        q_internal[1]) ** 2 - (1 / a4) * 0.25 * np.sin(q_internal[3]) ** 2,
                                         (1 / a1) * 0.25 * np.sin(q_internal[0]) * np.cos(q_internal[0]) + (
                                                     1 / a2) * ((q_internal[2] + 0.5) ** 2) * np.sin(
                                             q_internal[1]) * np.cos(q_internal[1]) - (1 / a3) * np.cos(
                                             q_internal[1]) * np.sin(q_internal[1]) + (1 / a4) * 0.25 * np.sin(
                                             q_internal[3]) * np.cos(q_internal[3]), expression*((-1/a1)*0.5*np.sin(q_internal[0])**2-(1/a2)*2*((0.5+q_internal[2])**2)*np.sin(q_internal[1])**2-(1/a3)*2*np.cos(q_internal[1])**2)],
                                        [(1 / a1) * 0.25 * np.sin(q_internal[0]) * np.cos(q_internal[0]) + (
                                                    1 / a2) * ((q_internal[2] + 0.5) ** 2) * np.sin(
                                            q_internal[1]) * np.cos(q_internal[1]) - (1 / a3) * np.cos(
                                            q_internal[1]) * np.sin(q_internal[1]) + (1 / a4) * 0.25 * np.sin(
                                            q_internal[3]) * np.cos(q_internal[3]),
                                         (-1 / a1) * 0.25 * np.cos(q_internal[0]) ** 2 - (1 / a2) * (
                                                     (q_internal[2] + 0.5) ** 2) * np.cos(q_internal[1]) ** 2 - (
                                                     1 / a3) * np.sin(q_internal[1]) ** 2 - (
                                                     1 / a4) * 0.25 * np.cos(q_internal[3]) ** 2, expression*((1/a1)*0.5*np.sin(q_internal[0])*np.cos(q_internal[0])+(1/a2)*2*((0.5+q_internal[2])**2)*np.sin(q_internal[1])*np.cos(q_internal[1])-(1/a3)*2*np.cos(q_internal[1])*np.sin(q_internal[1]))],
                                        [expression*((-1/a1)*0.5*np.sin(q_internal[0])**2-(1/a2)*2*((0.5+q_internal[2])**2)*np.sin(q_internal[1])**2-(1/a3)*2*np.cos(q_internal[1])**2),
                                         expression*((1/a1)*0.5*np.sin(q_internal[0])*np.cos(q_internal[0])+(1/a2)*2*((0.5+q_internal[2])**2)*np.sin(q_internal[1])*np.cos(q_internal[1])-(1/a3)*2*np.cos(q_internal[1])*np.sin(q_internal[1])),
                                         (expression**2)*((-1/a1)*np.sin(q_internal[0])**2-(1/a2)*4*((0.5+q_internal[2])**2)*np.sin(q_internal[1])**2-(1/a3)*4*np.cos(q_internal[1])**2)]])
                    bArr = np.array([Px[i] - 0.5 * np.cos(q_internal[0]) - (0.5 + q_internal[2]) * np.cos(
                        q_internal[1]) - 0.5 * np.cos(q_internal[3]),
                                     Py[i] - 0.5 * np.sin(q_internal[0]) - (0.5 + q_internal[2]) * np.sin(
                                         q_internal[1]) - 0.5 * np.sin(q_internal[3]),
                                     po**2-(0.5 * np.cos(q_internal[0]) + (0.5 + q_internal[2]) * np.cos(q_internal[1]) - 0.75)**2])
                    Mx, My, Mr = np.linalg.solve(coefArr, bArr)
                    delta_q[0] = (-Mx * 0.5 * np.sin(q_internal[0]) + My * 0.5 * np.cos(q_internal[0])-Mr*expression*np.sin(q_internal[0])) / (-a1)
                    delta_q[1] = (-Mx * (q_internal[2] + 0.5) * np.sin(q_internal[1]) + My * (
                                q_internal[2] + 0.5) * np.cos(q_internal[1]) - Mr*expression*2*(q_internal[2] + 0.5)*np.sin(q_internal[1])) / (-a2)
                    delta_q[2] = (Mx * np.cos(q_internal[1]) + My * np.sin(q_internal[1]) + Mr*expression*2*np.cos(q_internal[1])) / (-a3)
                    delta_q[3] = (-Mx * 0.5 * np.sin(q_internal[3]) + My * 0.5 * np.cos(q_internal[3])) / (-a4)
                    q_internal = q_internal + delta_q
                    delta = max(
                        abs(0.5 * np.cos(q_internal[0]) + (0.5 + q_internal[2]) * np.cos(q_internal[1]) + 0.5 * np.cos(
                            q_internal[3]) - Px[i]),
                        abs(0.5 * np.sin(q_internal[0]) + (0.5 + q_internal[2]) * np.sin(q_internal[1]) + 0.5 * np.sin(
                            q_internal[3]) - Py[i]))
                    if (delta < eps):
                        deltaArr[i] = delta
                        q = q_internal
                        iterArr[i] = counter
                        break
            animPlot.set_data([0, 0.5 * np.cos(q[0]), 0.5 * np.cos(q[0]) + (0.5 + q[2]) * np.cos(q[1]),
                               0.5 * np.cos(q[0]) + (0.5 + q[2]) * np.cos(q[1]) + 0.5 * np.cos(q[3])],
                              [0, 0.5 * np.sin(q[0]), 0.5 * np.sin(q[0]) + (0.5 + q[2]) * np.sin(q[1]),
                               0.5 * np.sin(q[0]) + (0.5 + q[2]) * np.sin(q[1]) + 0.5 * np.sin(q[3])])
            writer.grab_frame()

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(S, deltaArr)
    ax[0].plot(S, [eps]*100, '--')
    ax[0].set_title('Error value')
    ax[0].set_ylabel('Delta')
    ax[0].set_xlabel('S')
    ax[1].plot(S, iterArr)
    ax[1].set_title('Number of iterations')
    ax[1].set_ylabel('Iterations')
    ax[1].set_xlabel('S')
    plt.show()



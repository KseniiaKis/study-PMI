import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f_test(g):
    def rhs(x, u):
        return g-np.sin(u/4)
    return rhs

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
    return x[:steps+1], v[:steps+1], steps


def rk4_with_olp(x0, u0, h0, rhs, n_max, x_max, eps, eps_limit):

    dim = len(u0) if hasattr(u0, '__iter__') else 1
    if dim > 1:
        v = np.array([np.zeros(dim) for i in range(n_max)])
        v_double = np.array([np.zeros(dim) for i in range(n_max)])
        diff = np.array([np.zeros(dim) for i in range(n_max)])
    else:
        v = np.zeros(n_max)
        v_double = np.zeros(n_max)
        diff = np.zeros(n_max)
    c1 = np.zeros(n_max)
    c2 = np.zeros(n_max)
    x = np.zeros(n_max)
    s = np.zeros(n_max)
    f = rhs
    h = np.zeros(n_max)

    s[0] = 0
    x[0] = x0
    h[0] = h0
    v[0] = u0
    v_double[0] = u0
    n = 0
    while n < n_max-1:

        x[n+1], v[n+1] = rk4_step(x[n], h[n], v[n], f)

        h_half = h[n] / 2
        x_half_1, v_half = rk4_step(x[n], h_half, v[n], f)

        x_half_2, v_double[n+1] = rk4_step(x_half_1, h_half, v_half, f)
        diff[n+1] = v_double[n+1] - v[n+1]
        if (v[n + 1] > 4 * np.pi):
            v[n + 1] -= 8 * np.pi

        if dim > 1:
            s[n+1] = max(abs(diff[n+1] / (2 ** 4 - 1)))
        else:
            s[n+1] = abs(diff[n+1] / (2 ** 4 - 1))

        if (s[n+1] < (eps / (2 ** 5))):
            h[n+1] = h[n] * 2
            c1[n+1] = c1[n] + 1
        elif (s[n+1] > eps):
            h[n] = h_half
            c1[n + 1] = c2[n] + 1
            continue
        else:
            h[n+1] = h[n]
            c1[n + 1] = c1[n]
            c2[n + 1] = c2[n]

        if (x[n+1] > x_max):

            if(x[n] > x_max-eps_limit):
                break

            else:
                h[n] = x_max-x[n]
                n -= 1
        n += 1
    return x[:n+1], v[:n+1], v_double[:n+1], diff[:n+1], s[:n+1], h[:n+1], c1[:n+1], c2[:n+1], n

def plot_on_plane_test(x, u, v):
    fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig.suptitle('Сравнение численного и точного решений')
    axs[0].plot(x, v, '-r')
    axs[0].set_title('Численное решение:')
    axs[0].set_ylabel('V(x)')
    axs[1].plot(x, u, '-b')
    axs[1].set_title('Точное решение:')
    axs[1].set_ylabel('U(x)')
    axs[1].set_xlabel('x')
    plt.show()

def do_test():
    u0 = float(input("Введите начальное значение U0: "))
    h0 = float(input("Введите шаг h: "))
    n_max = int(input("Введите максимальное число шагов метода: "))
    x_max = float(input("Введите правую границу по х: "))
    x0 = 0
    g = 1.05
    rhs = f_test(g)
    choice = int(input("Введите 1, чтобы активировать контроль локальной погрешности: "))
    if choice:
        eps = float(input("Введите допустимое значение погрешности: "))
        eps_limit = float(input("Введите допустимое значение погрешности выхода за правую границу: "))
        x, v, v2, diff_v_v2, s, h, c1, c2, iters = rk4_with_olp(x0, u0, h0, rhs, n_max, x_max, eps, eps_limit)


        u = np.zeros(iters + 1)
        i = 0
        while i < iters + 1:
            u[i] = 8 * np.arctan((np.tan(x[i] * (g ** 2 - 1) / (8 * np.sqrt(g ** 2 - 1))) * np.sqrt(g ** 2 - 1) + 1) / g)

            if u[i] > 2 * np.pi:
                u[i] -= 2 * np.pi
            if u[i] > np.pi:
                u[i] -= 2 * np.pi
            if u[i] < -2 * np.pi:
                u[i] += 2 * np.pi
            if u[i] < -np.pi:
                u[i] += 2 * np.pi
            if v[i] > 2 * np.pi:
                v[i] -= 2 * np.pi
            if v[i] > np.pi:
                v[i] -= 2 * np.pi
            if v[i] < -2 * np.pi:
                v[i] += 2 * np.pi
            if v[i] < -np.pi:
                v[i] += 2 * np.pi
            i += 1



        u1 = 2 * np.arctan((np.tan(x * (g ** 2 - 1) / (2 * np.sqrt(g ** 2 - 1))) * np.sqrt(g ** 2 - 1) + 1) / g)
        u2 = 2 * np.arctan(1 / x) + np.pi / 2
        u01 = 2 * np.arctan((np.exp(x * 3 * np.sqrt(11) / 10) * (3 * np.sqrt(11) - 10) + 3 * np.sqrt(11) + 10) / (
                    1 - np.exp(x * 3 * np.sqrt(11) / 10)))
        u05 = 2 * np.arctan(
            (np.exp(x * np.sqrt(3) / 2) * (np.sqrt(3) - 2) + np.sqrt(3) + 2) / (1 - np.exp(x * np.sqrt(3) / 2)))
        u095 = 2 * np.arctan((np.exp(x * np.sqrt(39) / 20) * (np.sqrt(39) - 20) + np.sqrt(39) + 20) / (
                    19 * (1 - np.exp(x * np.sqrt(39) / 20))))


        u10 = 8 * np.arctan((np.tan(x * (g ** 2 - 1) / (8 * np.sqrt(g ** 2 - 1))) * np.sqrt(g ** 2 - 1) + 1) / g)
        u105 = 8 * np.arctan((np.exp(x * 3 * np.sqrt(11) / 10) * (3 * np.sqrt(11) - 10) + 3 * np.sqrt(11) + 10) / (
                1 - np.exp(x * 3 * np.sqrt(11) / 10)))
        u105 = 8 * np.arctan(
            (np.exp(x * np.sqrt(3) / 8) * (np.sqrt(3) - 2) + np.sqrt(3) + 2) / (1 - np.exp(x * np.sqrt(3) / 8)))
        u1095 = 8 * np.arctan((np.exp(x * np.sqrt(39) / 20) * (np.sqrt(39) - 20) + np.sqrt(39) + 20) / (
                19 * (1 - np.exp(x * np.sqrt(39) / 20))))

        diff_ui_vi = u - v
        table = pd.DataFrame({"xi": x, "vi": v, "ui": u, "ui-vi": diff_ui_vi})
        print(table)
        print("Справка: ")
        print(f"n = {iters}, b - xn = {x_max - x[iters]}")
        print(f"Max |ui-vi| = {max(diff_ui_vi)}, при x = {x[np.where(diff_ui_vi == max(diff_ui_vi))[0][0]]}")
    else:
        x, v, iters = rk4(x0, u0, h0, rhs, n_max, x_max)


        u = np.zeros(iters + 1)
        i = 0
        while i < iters + 1:
            u[i] = 8 * np.arctan((np.tan(x[i] * (g ** 2 - 1) / (8 * np.sqrt(g ** 2 - 1))) * np.sqrt(g ** 2 - 1) + 1) / g)

            
            if u[i] > np.pi:
                u[i] -= 2 * np.pi
            if u[i] < -2 * np.pi:
                u[i] += 2 * np.pi
            if u[i] < -np.pi:
                u[i] += 2 * np.pi
            if v[i] > 2 * np.pi:
                v[i] -= 2 * np.pi
            if v[i] > np.pi:
                v[i] -= 2 * np.pi
            if v[i] < -2 * np.pi:
                v[i] += 2 * np.pi
            if v[i] < -np.pi:
                v[i] += 2 * np.pi
            i += 1


        u1 = 2 * np.arctan((np.tan(x * (g**2 - 1)/(2 * np.sqrt(g**2 - 1))) * np.sqrt(g**2 - 1) + 1) / g)
        u2 = 2 * np.arctan(1/x) + np.pi/2
        u01 = 2 * np.arctan((np.exp(x*3*np.sqrt(11)/10)*(3*np.sqrt(11)-10)+3*np.sqrt(11)+10)/(1-np.exp(x*3*np.sqrt(11)/10)))
        u05 = 2 * np.arctan((np.exp(x*np.sqrt(3)/2)*(np.sqrt(3)-2)+np.sqrt(3)+2)/(1-np.exp(x*np.sqrt(3)/2)))
        u095 = 2 * np.arctan((np.exp(x*np.sqrt(39)/20)*(np.sqrt(39)-20)+np.sqrt(39)+20)/(19*(1-np.exp(x*np.sqrt(39)/20))))
        u10 = 8 * np.arctan((np.tan(x / 4 * (g ** 2 - 1) / (2 * np.sqrt(g ** 2 - 1))) * np.sqrt(g ** 2 - 1) + 1) / g)
        u101 = 8 * np.arctan((np.exp(x * 3 * np.sqrt(11) / 10) * (3 * np.sqrt(11) - 10) + 3 * np.sqrt(11) + 10) / (
                    1 - np.exp(x * 3 * np.sqrt(11) / 10)))
        u105 = 8 * np.arctan((np.exp(x * np.sqrt(3)/8) * (np.sqrt(3) - 2) + np.sqrt(3) + 2) / (1 - np.exp(x*np.sqrt(3)/8)))
        u1095 = 8 * np.arctan((np.exp(x * np.sqrt(39) / 20) * (np.sqrt(39) - 20) + np.sqrt(39) + 20) / (
                    19 * (1 - np.exp(x * np.sqrt(39) / 20))))

        diff_ui_vi = u - v
        table = pd.DataFrame({"xi": x, "vi": v, "ui": u, "ui-vi": diff_ui_vi})
        print(table)
        print("Справка: ")
        print(f"n = {iters}, b - xn = {x_max - x[iters]}")
        print(f"Max |ui-vi| = {max(abs(diff_ui_vi))}, при x = {x[np.where(abs(diff_ui_vi) == max(abs(diff_ui_vi)))[0][0]]}")
    plot_on_plane_test(x, u, v)



if __name__ == '__main__':
    do_test()


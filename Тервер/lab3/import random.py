import random
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import chi2

def geometric_cdf(x, p):
    return 1 - (1 - p)**(np.floor(x))

def detection(p):
    cycles = 1
    while random.random() >= p:
        cycles += 1
    return cycles

def play(p, num_simulations):
    n_cycles = [detection(p) for _ in range(num_simulations)]
    return n_cycles

def hypothesis_test(p, num_simulations, k_intervals, alpha):
    counts = Counter(play(p, num_simulations))
    yi = sorted(counts.keys())
    ni = [counts[y] for y in yi]
    nin = [count / num_simulations for count in ni]

    tmp_prev = 0
    sumqk = 0
    tmp = 0
    q = []
    R0 = 0

    for i in range(k_intervals):
        qk = 0
        nk = 0
        if i == k_intervals - 1:
            qk = 1 - sumqk
            tmp = len(yi)
        else:
            while qk < 1 / k_intervals and tmp < len(yi):
                qk += geometric_cdf(tmp + 1, p) - geometric_cdf(tmp, p)
                tmp += 1
        for j in range(tmp_prev, tmp):
            nk += ni[j]
        tmp_prev = tmp
        sumqk += qk
        q.append(qk)
        if qk > 0:
            R0 += (nk - num_simulations * qk) ** 2 / (num_simulations * qk)

    chi_square_value = chi2.ppf(1 - alpha, k_intervals - 1)

    return R0 <= chi_square_value, q

def main():
    p = float(input("Введите вероятность обнаружения объекта в каждом цикле обзора (0-1): "))
    if p < 0 or p > 1:
        print("Ошибка: Вероятность должна быть в диапазоне от 0 до 1")
        return
    num_simulations = int(input("Введите количество симуляций: "))
    k_intervals = 5
    alpha = 0.95

    accept = 0
    reject = 0
    q_values = []

    for _ in range(100):
        result, q = hypothesis_test(p, num_simulations, k_intervals, alpha)
        q_values.append(q)
        if result:
            accept += 1
        else:
            reject += 1

    print('alpha =', alpha)
    print('Ho: q =', q_values[-1])
    print('Гипотезу Ho приняли', accept, 'раз')
    print('Гипотезу Ho отклонили', reject, 'раз')

main()

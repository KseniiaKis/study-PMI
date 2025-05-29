import PySimpleGUI as sg
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import mainT
import scipy as sp

def geom(p):
    i = 1
    a = rd.random()

    while a >= p:
        i = i + 1
        a = rd.random()

    return i

headingsTabl = ["y_i","n_i","n_i/n"]
headingsNum1 = ["E","x_","|E - x_|", "D", "S^2", "|D-S^2|", "Me", "R"]
headingsMod = ["y_j", "P(j)", "n_i/n"]
table = []

layout = [  [sg.Text("Введите объём выборки"), sg.InputText("", k ='in0', size = (30, 20))],
            [sg.Text("Введите вероятность обнаружения"), sg.InputText("", k ='in1', size = (30, 20))],
            [sg.Button('Таблица'), sg.Button('Гипотеза'), sg.Button('Отмена')]]

window = sg.Window('Вариант 2', layout, font = 18)

while True:
    event, values = window.read()
    
    if event == 'Таблица':
              N = int(values[('in0')])
              stat = []
              counter = 0
              p = float(values[("in1")])
              for i in range(N):
                stat.append(geom(p))
              stat.sort()
              n = stat[N - 1]
              
              n_i = [0]*n

              for i in range (n):
                  for j in range(N):
                    if i + 1  == stat[j]:
                        n_i[i] = n_i[i] + 1
              
              table = [0]*n

              for i in range (n):
                    table[i] = [0]*3
                    table[i][0] = str(i + 1)
                    table[i][1] = str(n_i[i])
                    table[i][2] = str(n_i[i] / (N))
                                    
              mainT.create(table, headingsTabl)        

    if event == "Гипотеза":

        layout1 = [ [sg.Text("Введите количество отрезков"), sg.InputText("", k ='k1', size = (30, 20))],
                    [sg.Button('Далее') , sg.Button('Отмена')]]

        window1 = sg.Window('Вариант 2', layout1, font = 18)
        while True:
            event, values = window1.read()

            if event == 'Далее':
                k = int(values[('k1')])
                x = [0]*(k-1)
                layout2 = []

                for i in range(k-1):
                    layout2.append([sg.Text("Введите границу " + str(i+1)), sg.InputText("", k ='x' + str(i), size = (30, 20))])

                layout2.append([sg.Button('Далее1') , sg.Button('Отмена')])

                window1 = sg.Window('Вариант 2', layout2, font = 18)

                while True:
                    event, values = window1.read()

                    if event == 'Далее1':
                        for i in range(k-1):
                            x[i] = int(values[('x' + str(i))])
                        
                        a = 0.5
                        hi = sp.stats.chi2.ppf(1 - a, k-1)
                        print(hi)
                        accept = 0
                        reject = 0

                        for _ in range(1):
                            stat = []
                            for i in range(N):
                                stat.append(geom(p))
                            stat.sort()
                            n = stat[N - 1]

                            R0 = 0
                            N_i = [0]*k
                    
                            Q = [0]*(k)
                            tmp = 0
                        
                            for i in range (k):
                                for j in range(N ):
                                    if i == 0:
                                        if stat[j] <  x[0]:
                                            N_i[0] +=1   
                                    elif i == k - 1:
                                        if stat[j] >= x[k-2]:
                                            N_i[k-1] +=1
                                    else:
                                        if x[i-1] <= stat[j] < x[i]:
                                            N_i[i] +=1
                            if x[0] <= 0:
                                print("Ошибка")
                            else:
                                for o in range(1, x[0]):
                                    Q[0] += (1-p)**(o-1) * p
                            for i in range(1, k-1):
                                
                                for j in range(x[i-1], x[i]):
                                    if x[i] <= 0:
                                        Q[i] += 0
                                    else:
                                        Q[i] += (1-p)**(j-1) * p

                            for t in range(k):
                                tmp += Q[t]
                            Q[k-1] = (1 - tmp)

                            for i in range(k):
                                e = N*Q[i-1]
                                #print(a)
                                #print(N_i[i])
                                R0 = R0 + ((N_i[i] - e)**2 / e)

                            #print(R0)
                            if (R0 > hi):
                                reject += 1
                            else:
                                accept += 1

                        print("Набор q_i: ", Q)       
                        print("уровень значимости alfa = ", a)
                        print('Гипотезу Ho приняли', accept, 'раз')
                        print('Гипотезу Ho отклонили', reject, 'раз')

                    if event == sg.WIN_CLOSED or event == 'Отмена':
                        break

            if event == sg.WIN_CLOSED or event == 'Отмена':
                break

    if event == sg.WIN_CLOSED or event == 'Отмена':
            break
window.close()


import PySimpleGUI as sg
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import mainT

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
            [sg.Button('Таблица'), sg.Button('Числ. характеристики'), sg.Button('Отклонения'), sg.Button('Отмена')]]

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
        
    if event == 'Числ. характеристики':
        E = 1 / p
        x_ = 0
        D = (1 - p) / p**2
        S = 0
        F = []
        Stat = [0]

        for i in range(n):
            Stat.append(n_i[i] / N)

        for i in range(N):
            x_ = x_+ stat[i]
        x_ = x_ / N

        for i in range(N):    
            S = S + (stat[i] - x_) ** 2

        F=list(np.random.geometric(p, max(100, N)))
        
        S = S / N
        if N == 1:
            R = stat[N - 1]
        else:
            R = stat[N - 1] - stat[0] 

        Me = 0

        if (N % 2 == 1):
            Me = stat[ (N-1) // 2 ] 
        else:

            Me = ( stat[ (N - 1) // 2] + stat[ ((N - 1) // 2) + 1 ]) /2

        Teor = []
        FTeor =[]
        for i in range(1, 101):
            a = (1-p)**(i-1) * p
            Teor.append(a)
            FTeor.append(a)

        for i in range(100):
            FTeor[i] = FTeor[i] + FTeor[i-1]

        FSta = [0]*len(Stat)

        FSta = Stat
        for i in range(1, len(FSta)):
            FSta[i] = (FSta[i] + FSta[i - 1])
        
        Otkl = []

        for i in range (1, n):
            Otkl.append(abs(FTeor[i] - FSta[i+1]))

        xT = []
        yT = []
        counter = 0

        for i in range(100):
            xT.append(counter)
            yT.append(FTeor[i])
            counter = counter + 1
            xT.append(counter)
            xT.append(None)
            yT.append(FTeor[i])
            yT.append(None)
        
        xS = [-1, 0, None]
        yS = [0, 0, None]
        counter1 = 0
        for i in range(1,n+1):
            xS.append(counter1)
            yS.append(FSta[i])
            counter1 = counter1 + 1
            xS.append(counter1)
            xS.append(None)
            yS.append(FSta[i])
            yS.append(None)

        tableNum1 = [[f'{E:.2f}', f'{x_:.2f}', f'{abs(E - x_):.2f}', f'{D:.2f}', f'{S:.2f}',f'{abs(D - S):.2f}', str(Me), str(R)]]
        mainT.create(tableNum1, headingsNum1)

        plt.plot(xT,yT, 'b')
        plt.plot(xS,yS, 'g')
        plt.xlim(-1, n)
        plt.show()

    if event == 'Отклонения':
        tableNum2 = [0]*n

        for i in range (n):
                    tableNum2[i] = [0]*3
                    tableNum2[i][0] = str(i + 1)
                    tableNum2[i][1] = f'{Teor[i]:.2f}'
                    tableNum2[i][2] = f'{n_i[i] / (N):.2f}'

        Otkl.sort()
        print("Максимальное отклонение = " + str(Otkl[len(Otkl)-1]))
        mainT.create(tableNum2, headingsMod)

    if event == sg.WIN_CLOSED or event == 'Отмена':
            break
window.close()


import PySimpleGUI as sg
import random as rd
import mainT

def geom(p):
    i = 1
    a = rd.random()

    while a >= p:
        i = i + 1
        a = rd.random()

    return i

headings = ["y_i","n_i","n_i/n"]
table = []

layout = [  [sg.Text("Введите объём выборки"), sg.InputText("", k ='in0', size = (30, 20))],
            [sg.Text("Введите вероятность обнаружения"), sg.InputText("", k ='in1', size = (30, 20))],
            [sg.Button('Далее'), sg.Button('Отмена')]]

window = sg.Window('Вариант 2', layout)

while True:
    event, values = window.read()
    
    if event == 'Далее':
              N = int(values[('in0')])
              stat = []
              Len = []
              counter = 0
              for i in range(N):
                stat.append(geom(float(values[("in1")])))
                Len.append(stat[i])
              Len.sort()
              n = Len[N - 1]
              
              n_i = [0]*n

              for i in range (n):
                  for j in range(N):
                    if i + 1  == stat[j]:
                        n_i[i] = n_i[i] + 1
                #   counter = counter + n_i[j]
              
              table = [0]*n

              for i in range (n):
                    table[i] = [0]*3
                    table[i][0] = str(i + 1)
                    table[i][1] = str(n_i[i])
                    table[i][2] = str(n_i[i] / (N))
                                    
              mainT.create(table, headings)

    if event == sg.WIN_CLOSED or event == 'Отмена':
            break
window.close() 


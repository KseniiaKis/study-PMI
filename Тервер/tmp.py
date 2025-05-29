import PySimpleGUI as sg
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = [0]*101
y = [0]*101
z = [0]*101

for i  in range(0,101):
    x[i] = 1 + i/100
    y[i] = 2 + i/100
    z[i] = -np.pi**4*x[i]**4*np.cos(np.pi*x[i]*y[i])
    
z.sort()   
    
print(z[100]/12)
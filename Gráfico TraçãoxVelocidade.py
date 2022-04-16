# -*- coding: utf-8 -*-
"""
TRAINEE BURGING GOOSE AERO DESEING UFPR.


Gráfico tração em função da velocidade hélice 20x8E
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'dados.txt'  # importando arquivo txt com os dados convertidos
columnsnames = ['x1', 'y1']  # Nomeando as colunas

df = pd.read_csv(file, skiprows=1, names=columnsnames, sep='\s+')

lista_x = df["x1"].tolist()  # Transformando coluna x em lista
lista_y = df["y1"].tolist()  # Transformando coluna y em lista


x = np.array(lista_x)  # Inserindo pontos da velocidade em x

y = np.array(lista_y)  # Inserindo pontos da tração em y
 
poly = np.polyfit(x, y, 2)  # Ajustando polinomio

a, b, c = poly  

print("Coeficientes:")
print(a, b, c)  # Print dos coeficientes 

p = 1.206  # Densidade local calculada
p0 = 1.225  # Densidade nível do mar

#plt.scatter(x, y, label='tração')
plt.plot(x, a*x**2 + b*x + c, color='k', label='h nível do mar')
plt.plot(x, (a*x**2 + b*x + c)*(p/p0), color='darkcyan', label='h calculado')
plt.title('Scorpion 4020KV, APC20X8E a 5000RPM')
plt.legend()
plt.xlabel('V (m/s)')
plt.ylabel('T (N)')
plt.ylim(0, 50)
plt.xlim(0, 26)
plt.yticks(np.arange(0, 55, 5))
plt.xticks(np.arange(0, 28, 2))
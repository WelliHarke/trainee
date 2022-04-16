# -*- coding: utf-8 -*-
"""
TRAINEE DESEMPENHO - BURGING GOOSE AERO DESEING UFPR.

Calcular altitude densidade e a densidade do ar para diferentes alturas.
Temperatura local = 20.5°C   Pressão local = 1016.5 hPa
"""

print("-"*90)
print("INSIRA OS DADOS:")
print()

a = float(input("Pressão atmosférica do ar local em hPa: ", ))
b = float(input("Temperatura local do ar em °C: "))

print()
  
T0 = 288.15  # Temp padrao nivel mar
p0 = 101325  # Pressao padrao mar
L = 0.0065  # Taxa gradiente 
R = 8.3144598 # Gas ideal
g = 9.80665  # Gravidade
M = 0.028964  # Massa molar
TK = b + 273.15 # Conversão para K
P = a*100 # Conversão para Pa

h = (T0/L)*(1-((P/p0)/(TK/T0))**0.234978)

print('-> A altitude densidade para os dados informados é de:', round(h,2), "metros.")
print("-"*90)
print("SENDO A ALTITUDE DENSIDADE", round(h,2),"METROS, TEMOS:")
print()
Th = T0 - L*h                      # Temperatura na altitude h (K)
print("A temperatura do ar nessa altitude como: ",round(Th,2),"K.")
print()
ph = p0*(1 - L*h/T0)**(g*M/(R*L))  # Pressão na altitude h (Pa)
print("A pressão do ar nessa altitude como: ",round(ph,2),"Pa.")
print()
p = ph*M/(R*Th)                    # Densidade do ar na altitude h (kg/m³)
print("-> A densidade do ar nessa altitude como: ",round(p,3),"kg/m³.")
print("-"*90)

h2 = 0
Th2 = T0 - L*h2
ph2 = p0*(1 - L*h2/T0)**(g*M/(R*L))
p2 = ph2*M/(R*Th2) 

print("OBS: A DENSIDADE DO AR PARA UMA ALTITUDE DENSIDADE A NÍVEL DO MAR",
      "É DE", round(p2,3), "KG/M³.")
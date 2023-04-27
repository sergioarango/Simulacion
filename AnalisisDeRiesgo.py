# -*- coding: utf-8 -*-
"""
Simulación de análisis de riesgo
"""
#%% librerías
import numpy as np
import matplotlib.pyplot as plt

#%%Parámetro
PrecioVenta=249
GA=400000
GP=600000
N=1000
A=80; B=100
miu=15000; sigma=4500

#%%Valores iniciales
Utilidadv=[]
Count=0

#%%simulación
for i in range (N):
    R=np.random.uniform(0,1)
    if 0<=R<0.1:
        C1=43
    if 0.1<=R<0.3:
        C1=44
    if 0.3<=R<0.7:
        C1=45
    if 0.7<=R<0.9:
        C1=46
    if 0.9<=R<=1:
        C1=47
    C2=np.random.uniform(A,B)
    x=np.random.normal(miu, sigma)
    Utilidad=(PrecioVenta-C1-C2)*x-GA-GP
    Utilidadv.append(Utilidad)

for element in Utilidadv:
    if element<0:
        Count=Count+1

riesgo=(Count/N)*100

print("El riesgo de sacar al mercado la nueva impresora es de "+str(riesgo)+"%")

plt.hist(Utilidadv)
plt.xlabel("Utilidad")
plt.ylabel("Frecuencia")

plt.show()




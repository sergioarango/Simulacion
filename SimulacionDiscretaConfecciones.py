##### Ejercicio confecciones #######

#librerías necesarias
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

#Parámetros del modelo
Teladisponible=0
Simulaciones=10
Tcortada=20                                         #Cada vez que llega tela llegan 20 metros
tiempolabordia=8                                    #tiempo laborado en un dia
Tacum=0                                             #Variable que calcula el tiempo acumulado
Chaquetas=0                                         #Numero de chaquetas
Blusas=0                                            #Numero de blusas
TBlusas=1
TChaquetas=1.5
confeccionistas=15

resultadosBlusas=pd.DataFrame()
resultadosChaquetas=pd.DataFrame()


for j in range(Simulaciones):
    LLegaTela=[]
    Tacum=0
    Chaquetas=0
    Blusas=0
    while Tacum<=tiempolabordia:
        LLegaTelaint=stats.uniform.rvs(1/60,20/60,size=1)         #La llegada de la tela es una variable uniforme continua entre 1 y 20 minutos
        LLegaTela.append(LLegaTelaint)
        Teladisponible=Teladisponible+Tcortada                    #Cada vez que corto tela le sumo 20m a la tela disponible
        Tacum=Tacum+LLegaTelaint
    
    #####Distribuciones 
    
    ChaquetasConfeccionistas=[]
    BlusasConfeccionistas=[]
    Confeccionistas=[]
    resultadosBlusas['Simulación: '+str(j)]=None
    resultadosChaquetas['simulación: '+str(j)]=None
    for i in range (confeccionistas):
        Confeccionistas.append(i)
        Tacum=0
        Blusas=0
        Chaquetas=0
        Tacumv=[]
        while Tacum<=tiempolabordia:
            if Teladisponible>0:
                SeleccionPrenda=stats.uniform.rvs(0,1,size=1)
            if SeleccionPrenda<0.5:
                Teladisponible=Teladisponible-TBlusas                #Debo restar a la tela disponible, la tela que utilicé para confeccionar blusas
                tiempoblusa=stats.uniform.rvs(5/60,15/60, size=1)
                Tacum=Tacum+tiempoblusa
                Blusas=Blusas+1
            if SeleccionPrenda>0.5:
                Teladisponible=Teladisponible-TChaquetas              #Debo restas a la tela disponible, la tela que me gasto haciendo una chaqueta
                tiempochaquetas=stats.uniform.rvs(10/60,20/60,size=1)
                Tacum=Tacum+tiempochaquetas
                Chaquetas=Chaquetas+1 
            print("tiempos de onfección del confeccionista "+str(i))
            print(Tacum)
        ChaquetasConfeccionistas.append(Chaquetas)
        BlusasConfeccionistas.append(Blusas)
    resultadosBlusas['Simulación: '+str(j)]=BlusasConfeccionistas
    resultadosChaquetas['simulación: '+str(j)]=ChaquetasConfeccionistas
  
    
plt.bar(Confeccionistas, BlusasConfeccionistas)   

 
print(resultadosBlusas)
print(resultadosChaquetas)


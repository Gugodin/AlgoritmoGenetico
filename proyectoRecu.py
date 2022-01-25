import math
from typing import Match
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats

from pandas.io import excel


datos = pd.read_csv('193257 GUTIERREZ ESPINOSA_C1.A2R.csv')

conjuntoCiudades = list(set(datos['Ciudad']))
conjuntoCiudades.sort()
ciudadesClasificadas = list(datos.groupby(['Ciudad']))
colores = ['red','green','#EC407A','brown','orange','yellow','grey','blue','pink','purple','aqua','gold']
allCiudades = list(datos['Ciudad'])
cantidadVotadas = []


for i in range (0,len(conjuntoCiudades)):
    cantidadVotadas.append(allCiudades.count(conjuntoCiudades[i]))


figure = plt.figure(figsize=(15,10))
separacion = ([0,0,0,0,0,0,0,0,0,0,0,0.1])
ax = plt.subplot(2,3,1)
ax.pie(cantidadVotadas,labels=conjuntoCiudades,colors=colores,autopct="%0.1f %%",pctdistance=0.85,explode = separacion)
ax.set_title('Participaciones por ciudad')


todasEstaturas = list(datos.Estatura)
todasEstaturas.sort()

datoMax = max(todasEstaturas)
datosMin = min(todasEstaturas)
rango = datoMax - datosMin

numClases = round(1 + 3.3 * (math.log(len(todasEstaturas),10)))

anchoClase = round(rango/numClases,4)

tablaDeFrecuencia = []

for i in range(7):
    tablaDeFrecuencia.append([])

def sacarLimites ():
    aux = datosMin
    relleno = 1
    for i in range(0, 9):
        tablaDeFrecuencia[0].append(relleno)
        relleno = relleno + 1
        tablaDeFrecuencia[1].append(round(aux, 2))
        aux = aux + anchoClase
        tablaDeFrecuencia[2].append(round(aux, 2))

def sacarMarcaDeClase ():
    for i in range(0, 9):
        marcaDeCLase = (tablaDeFrecuencia[1][i] + tablaDeFrecuencia[2][i])/2
        tablaDeFrecuencia[3].append(round(marcaDeCLase,2))

def sacarFrecuenciaAbsoluta ():
    contador = 0
    for i in range(0, 9):
        for x in range(0,len(todasEstaturas)):
            if i == 0:
                if todasEstaturas[x] >= tablaDeFrecuencia[1][i] and todasEstaturas[x] <= tablaDeFrecuencia[2][i]:
                    contador = contador+1
            if i > 0:
                if todasEstaturas[x] > tablaDeFrecuencia[1][i] and todasEstaturas[x] <= tablaDeFrecuencia[2][i]:
                    contador = contador + 1
        tablaDeFrecuencia[4].append(contador)
        contador = 0

def sacarFrecuenciaRelativa():
    for i in range(0, 9):
        frecuenciaRelativa = (tablaDeFrecuencia[4][i]/len(todasEstaturas))*100
        tablaDeFrecuencia[5].append(round(frecuenciaRelativa,2))

def sacarFrecuenciaRelativaAcu ():
    acumulador = 0
    for i in range(0, 9):
        if i < 8:
            acumulador = acumulador + tablaDeFrecuencia[5][i]
            tablaDeFrecuencia[6].append(round(acumulador,2))
        if  i == 8:
            acumulador = acumulador + tablaDeFrecuencia[5][i]
            tablaDeFrecuencia[6].append(round(acumulador))

sacarLimites()
sacarMarcaDeClase()
sacarFrecuenciaAbsoluta()
sacarFrecuenciaRelativa()
sacarFrecuenciaRelativaAcu()

bins = tablaDeFrecuencia[3]

ax1 =plt.subplot(2,3,2)
listaOjiva = [[],[]]
listaOjiva[0].append(0)
listaOjiva[1].append(0)
for i in range(1,9):
    listaOjiva[0].append(tablaDeFrecuencia[3][i])
    listaOjiva[1].append(tablaDeFrecuencia[6][i])
ax1.plot(listaOjiva[0],listaOjiva[1])
ax1.set_xlabel('Estatura')
ax1.set_ylabel('Frecuencia Relativa')
ax1.set_title('OJIVA')


ax4 =plt.subplot(2,3,3)
listaPoligono = [[],[]]
listaPoligono[0].append(0)
listaPoligono[1].append(0)
for i in range(1,9):
    listaPoligono[0].append((tablaDeFrecuencia[3][i]))
    listaPoligono[1].append((tablaDeFrecuencia[4][i]))
ax4.plot(listaPoligono[0],listaPoligono[1],'x-')
ax4.set_title('POLÍGONO DE FRECUENCIA')
ax4.set_xlabel('Estatura')
ax4.set_ylabel('Frecuencia Absoluta')

ax3 =plt.subplot(2, 3,4)
ax3.hist(todasEstaturas,bins,edgecolor='black')
ax3.axvline(round(stats.mean(todasEstaturas),2), color='#F7BD65', label='Media', linewidth=2)
ax3.axvline(stats.median(todasEstaturas), color='black', label='Mediana', linewidth=4)
ax3.axvline(stats.mode(todasEstaturas), color='#8E3AA1', label='Moda', linewidth=3)
ax3.legend()
ax3.set_title('HISTOGRAMA')


listaBarras = [datos['Edad'],datos['Estatura']]
ax2 =plt.subplot(2, 3, 5)
ax2.bar(listaBarras[0], listaBarras[1])
ax2.set_xlabel('Edades')
ax2.set_ylabel('Estatura')
ax2.set_title('GRÁFICA DE CHIAPAS')


varianza = stats.variance(todasEstaturas)
desviacion= math.sqrt(varianza)

ax5 =plt.subplot(2,3,6)
ax5.text(0.2, .7, 'Rango: {0}'.format(rango), fontsize=15)
ax5.text(0.2, .8, 'Varianza: {0}'.format(round(varianza, 4)), fontsize=15)
ax5.text(0.2, .9, 'Desviación estandar: {0}'.format(round(desviacion, 4)), fontsize=15)
ax5.axis('off')


def generarExcel():
    datos = pd.DataFrame (
        {
            'clase' : tablaDeFrecuencia[0],
            'Lim Inferior' : tablaDeFrecuencia[1],
            'Lim Sup' : tablaDeFrecuencia[2],
            'MarcaDeClase' : tablaDeFrecuencia[3],
            'Frecuencia Absoluta' : tablaDeFrecuencia[4],
            'Frecuencia Relativa' : tablaDeFrecuencia[5],
            'Frecuencia Relativa Acumulada' : tablaDeFrecuencia[6]
        }
    )
    
    excel = datos.to_excel('Tabla de frencuencia.xlsx',index=False)




generarExcel()

plt.subplots_adjust(wspace=0.6)
plt.show()


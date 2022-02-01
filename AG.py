import math
import random  
import string
import tkinter as tk
from tkinter import *
from unicodedata import decimal
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from individuo import Ind



#Definicion de parametros
#x**2+2*x+3
#Simbolos validos para funcion: +,-,*,/,**,(,)
# InitialPopulation = 5
# MaxPopulation = 10
# ProbMutation = 0.1
# ProbMutationGen = 0.05

Generations = {}
GenerationsPoda = {}
Population:Ind = []

interval = {
    'x':[],
    'y':[]
}

#resolution = 0.05

def transform(fx:str):
    f = list(fx.replace('^','**'))

    for i in range(len(f)):
        
        if i < len(f)-1:
            if f[i].isdecimal() and f[i+1] == 'x':
                f.insert(i+1,'*')
        if i > 0 :     
            if f[i] == '(' and (f[i-1].isdecimal() or f[i-1].isalpha()):

                f.insert(i,'*')   

    f = ''.join(f)
        
    return f


def generatePopulation():

    global Population

    lengthIntervalX = interval['x'][1] - interval['x'][0]
    lengthValuesX = (lengthIntervalX/resolution)+1
    
    lengthIntervalY = interval['y'][1] - interval['y'][0]
    lengthValuesY = (lengthIntervalY/resolution)+1

    numBitsX = 1
    numBitsY = 1
    #Verificar el numero de bits de X y Y
    
    while(True):
        if lengthValuesX <= 2**numBitsX:
            break
        numBitsX = numBitsX + 1
        
    while(True):
        if lengthValuesY <= 2**numBitsY:
            break
        numBitsY = numBitsY + 1

    
    #Generamos los individuos con la clase Ind
    i = 0
    while(i < InitialPopulation):

        ind = Ind([numBitsX,numBitsY],[interval['x'][0],interval['y'][0]],resolution,None) 

        if ind.decimal['x'] < lengthValuesX and ind.decimal['y'] < lengthValuesY:
            Population.append(ind)
            i+=1
                  
    return [numBitsX,numBitsY,lengthValuesX,lengthValuesY]


def mating(numB,lengthValuesX,lengthValuesY):
    
    global Population

    pTemp = []

    for i in range(len(Population)):
        pTemp.append(Population[i])
    

    parents = []
    
    #Generamos parejas de 2 o 1 aleatoriamente

    while len(pTemp) != 0:
        partner1 = pTemp.pop(random.randint(0,len(pTemp)-1))

        if len(pTemp) != 0:
            partner2 = pTemp.pop(random.randint(0,len(pTemp)-1))
            parents.append([partner1,partner2])
        else:
            parents.append([partner1])


    #Generar a los hijos con la cruza y mutacion
    children = cruza(parents,numB,lengthValuesX,lengthValuesY)
    #Meter a los hijos a la poblacion
    

    for i in range(len(children)):
        Population.append(children[i])


def cruza (parents,numB,lengthValuesX,lengthValuesY):
    global Population
    children = []

    for i in range(len(parents)):
        spotCruzaX =  random.randint(1,len(parents[i][0].bits['x'])-1)
        spotCruzaY = random.randint(1,len(parents[i][0].bits['y'])-1)
       

        if len(parents[i]) !=1:
            name1 = ''
            name2 = ''

            p1 = parents[i][0].bits
            p2 = parents[i][1].bits

            
           

            name1 = name1 + parents[i][0].id + parents[i][1].id
            name2 = name2 + parents[i][1].id + parents[i][0].id


            child1BitsX = []
            child1BitsY = []

            for x in range(len(p1['x'])):

                if x >= spotCruzaX:
                    child1BitsX.append(p2['x'][x])
                else:
                    child1BitsX.append(p1['x'][x])
                    
            for y in range(len(p1['y'])):

                if y >= spotCruzaY:
                    child1BitsY.append(p2['y'][y])
                else:
                    child1BitsY.append(p1['y'][y])

            child1Bits ={
                'x':child1BitsX,
                'y':child1BitsY
                }
            
            child2BitsX = []
            child2BitsY = []

            for x in range(len(p1['x'])):

                if x >= spotCruzaX:
                    child2BitsX.append(p1['x'][x])
                else:
                    child2BitsX.append(p2['x'][x])
                    
            for y in range(len(p1['y'])):

                if y >= spotCruzaY:
                    child2BitsY.append(p1['y'][y])
                else:
                    child2BitsY.append(p2['y'][y])

            child2Bits ={
                'x':child2BitsX,
                'y':child2BitsY
                }

            
            
            #Ahora vemos cual de los hijos mutara o no

            pMCh1 = round(random.uniform(0,1),2)
            pMCh2 = round(random.uniform(0,1),2)
            
            

            if pMCh1 <= ProbMutation:
                #Mutara el hijo 1
                #Generar probabilidades de mutacion por gen             

                for i in range(len(p1['x'])):
                    pMGx = round(random.uniform(0,1),3)
                    
                    if pMGx <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        
                        if child1Bits['x'][i] == 0:
                            child1Bits['x'][i] = 1
                        elif child1Bits['x'][i] == 1:
                            child1Bits['x'][i] = 0

                for i in range(len(p1['y'])):
                    pMGy = round(random.uniform(0,1),3)
                    
                    if pMGy <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        
                        if child1Bits['y'][i] == 0:
                            child1Bits['y'][i] = 1
                        elif child1Bits['y'][i] == 1:
                            child1Bits['y'][i] = 0
            

            if pMCh2 <= ProbMutation:
                #Mutara el hijo 2
                #Generar probabilidades de mutacion por gen             

                for i in range(len(p1['x'])):
                    pMGx = round(random.uniform(0,1),3)
                    
                    if pMGx <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        
                        if child2Bits['x'][i] == 0:
                            child2Bits['x'][i] = 1
                        elif child2Bits['x'][i] == 1:
                            child2Bits['x'][i] = 0

                for i in range(len(p1['y'])):
                    pMGy = round(random.uniform(0,1),3)
                    
                    if pMGy <= ProbMutationGen:
                        #Va a mutar en esta posicion
                      
                        if child2Bits['y'][i] == 0:
                            child2Bits['y'][i] = 1
                        elif child2Bits['y'][i] == 1:
                            child2Bits['y'][i] = 0
            
        

            child1 = Ind(None,[interval['x'][0],interval['y'][0]],resolution,name1,child1Bits)
            child2 = Ind(None,[interval['x'][0],interval['y'][0]],resolution,name2,child2Bits)

          

            if child1.decimal['x'] < lengthValuesX and child1.decimal['y'] < lengthValuesY:
                children.append(child1)

            if child2.decimal['x'] < lengthValuesX and child2.decimal['y'] < lengthValuesY:
                children.append(child2)


        else:
            
            name1 = ''
            name1 = name1 + parents[i][0].id + parents[i][0].id

            child1Bits = parents[i][0].bits
            
            for i in range(len(p1['x'])):
                    pMGx = round(random.uniform(0,1),3)
                    
                    if pMGx <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        
                        if child1Bits['x'][i] == 0:
                            child1Bits['x'][i] = 1
                        elif child1Bits['x'][i] == 1:
                            child1Bits['x'][i] = 0

            for i in range(len(p1['y'])):
                pMGy = round(random.uniform(0,1),3)
               
                if pMGy <= ProbMutationGen:
                    #Va a mutar en esta posicion
                  
                    if child1Bits['y'][i] == 0:
                        child1Bits['y'][i] = 1
                    elif child1Bits['y'][i] == 1:
                        child1Bits['y'][i] = 0
            

            child1 = Ind(None,[interval['x'][0],interval['y'][0]],resolution,name1,child1Bits)
            
            

            if child1.decimal['x'] < lengthValuesX and child1.decimal['y'] < lengthValuesY:
                children.append(child1)

   
    return children


def poda():
    global Population

    numEliminations = len(Population) - MaxPopulation

    aptitudes = []
    
    for i in range(len(Population)):
        aptitudes.append(Population[i].aptitude)

    for i in range(numEliminations):
        # print(f'Minimo: {min(aptitudes)}')
        for x in range(len(aptitudes)):

            if aptitudes[x] == min(aptitudes):
                Population.pop(x)
                aptitudes.pop(x)
                break
    # print(aptitudes)
#interfas grefica mas los datos

def valoresG(poblacionI, poblacionM, minimoX, maximoX, minimoY, maximoY, probabilidadM, probabilidadG, resolucion, valorgene):
    global InitialPopulation 
    global MaxPopulation
    global ProbMutation
    global ProbMutationGen 
    global resolution
    global intervaloMinimoX
    global intervaloMaximoX
    global intervaloMinimoY
    global intervaloMaximoY
    global valorXmin
    global valorXmax
    global valorYmin
    global valorYmax
    global numGeneration
    
    
    InitialPopulation = poblacionI
    MaxPopulation = poblacionM 
    ProbMutation = probabilidadM
    ProbMutationGen = probabilidadG
    resolution = resolucion
    valorXmin = minimoX
    valorXmax =  maximoX
    valorYmin = minimoY
    valorYmax = maximoY
    numGeneration = valorgene
    
    interval['x'].append(valorXmin)
    interval['x'].append(valorXmax)
    interval['y'].append(valorYmin)
    interval['y'].append(valorYmax)
    
    for i in range(numGeneration):
        Generations.update({f'gen{i+1}':[]})

    for i in range(numGeneration):
        GenerationsPoda.update({f'gen{i+1}':[]})

    # print(Generations) 
    
    numB = generatePopulation()


    for i in range(numGeneration):

        mating(numB,numB[2],numB[3])
        
        
        
        for x in range(len(Population)):
            Generations[f'gen{i+1}'].append(Population[x])
        if len(Population) > MaxPopulation:
            
            #Inicia poda
            poda()

        for x in range(len(Population)):
            GenerationsPoda[f'gen{i+1}'].append(Population[x])


    promedioList = []
    bestList = []
    worstList = []
    bestInd = []

    for i in range(numGeneration):

        aptitudes = []
    
        for x in range(len(Generations[f'gen{i+1}'])):
            aptitudes.append(Generations[f'gen{i+1}'][x].aptitude)
    
        bestList.append(max(aptitudes))
        worstList.append(min(aptitudes))
        
        
        #Sacar promedio
        prom = 0

        for y in range(len(aptitudes)):
            prom += aptitudes[y]
        
        promedioList.append(prom/len(aptitudes))

    
    temp = Generations[f'gen{numGeneration}']
    aptitudes = []
    
    for x in range(len(Generations[f'gen{numGeneration}'])):
        aptitudes.append(Generations[f'gen{numGeneration}'][x].aptitude)

    for i in range(4):
        mejorAp = max(aptitudes)
        indexMejorAp = aptitudes.index(mejorAp)
        aptitudes.pop(indexMejorAp)
        indMejor = temp.pop(indexMejorAp)
        bestInd.append(indMejor)

    for i in range(len(bestInd)):
        print(bestInd[i].toString())


    
    gene = []
    tabla = [['Bits','i','Fenotipo','Aptitud']]

    for i in range(4):
        currentInd = bestInd[i]
        fila = []
        bits = f'BitsX: {str(currentInd.bits["x"])}\nBitsY: {str(currentInd.bits["y"])}'
        decimal = f'DecimalX: {str(currentInd.decimal["x"])}\nDecimalY: {str(currentInd.decimal["y"])}'
        fenotipo = f'FenotipoX: {str(currentInd.fenotipe["x"])}\nFenotipoY: {str(currentInd.fenotipe["y"])}'
        aptitud = f'Aptitud: {str(currentInd.aptitude)}'

        fila.append(bits)
        fila.append(decimal)
        fila.append(fenotipo)
        fila.append(aptitud)

        tabla.append(fila)

    for i in range(len(Generations)):
        gene.append(i+1)
    # print(gene)


    figure = plt.figure(figsize=(15,10))
    ax = plt.subplot(2,1,1)
    ax.plot( gene,promedioList, label='Promedio',marker='.')  # Plot some data on the (implicit) axes.
    ax.plot( gene,worstList, label='Peor',marker='.')  # etc.
    ax.plot( gene,bestList,label='Mejor',marker='.')

    blue_line = mlines.Line2D([], [], color='blue', 
                          markersize=15, label='Promedio')
    red = mlines.Line2D([], [], color='orange', 
                          markersize=15, label='Peor')
    yel = mlines.Line2D([], [], color='green', 
                          markersize=15, label='Mejor')
    ax.legend(handles=[blue_line,red,yel])

    ax2 = plt.subplot(2,1,2)
    ax2.axis('tight')
    ax2.axis('off')
    table = ax2.table(cellText = tabla, loc = "center", cellLoc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1,3)
    ax2.set_title('\n Tabla de mejores individuos')

    plt.show()  

    generateEvolitionByInd()


   

def generateEvolitionByInd():

    for i in range(len(GenerationsPoda)):

        currentGeneration = GenerationsPoda[f'gen{i+1}']

        figure2 = plt.figure(figsize=(15,10))

        ax = plt.subplot(1,1,1)
        ax.set_title(f'Generacion{i+1}')
        # ax.xaxis.set_major_formatter([-3,3])

        print(len(currentGeneration))
        ax.plot(interval['x'][0],interval['y'][0] ,marker='o',lw = 0,visible=False)
        ax.plot(interval['x'][1],interval['y'][1] ,marker='o',lw = 0,visible=False)
        for x in range(len(currentGeneration)):

            ax.plot(currentGeneration[x].fenotipe['x'],currentGeneration[x].fenotipe['y'] ,marker='o',lw = 0)
        
        # if i+1 ==  10:

        #     for x in range(len(currentGeneration)):

        #         print(currentGeneration[x].toString())
            

        plt.savefig(f'./prue/img{i}')
        plt.show()
      
    
def inicio():
    window = Tk()
    window.title("Algoritmos Geneticos")
    window.geometry('600x300')
    #generacion
    lbl = Label(window, text="Numero Generacion: ")
    lbl.grid(column=0, row=9)
    valor10 = Entry(window,width=10)
    valor10.grid(column=1, row=9)
    valor10.focus()

    #PI
    lbl = Label(window, text="Poblacion Inicial: ")
    lbl.grid(column=0, row=0)
    valor1 = Entry(window,width=10)
    valor1.grid(column=1, row=0)
    valor1.focus()
    #PM
    lb2 = Label(window, text="Poblacion Maxima: ")
    lb2.grid(column=0, row=1)
    valor2 = Entry(window,width=10)
    valor2.grid(column=1, row=1)
    valor2.focus()
    #IX
    lb3 = Label(window, text="Intervalo Minimo de 'X': ")
    lb3.grid(column=0, row=2)
    valor3 = Entry(window,width=10)
    valor3.grid(column=1, row=2)
    valor3.focus()
    
    lb4 = Label(window, text="Intervalo Maximo de 'X': ")
    lb4.grid(column=0, row=3)
    valor4 = Entry(window,width=10)
    valor4.grid(column=1, row=3) 
    valor4.focus()
    #IX
    lb5 = Label(window, text="Intervalo Minimo de 'Y': ")
    lb5.grid(column=0, row=4)
    valor5 = Entry(window,width=10)
    valor5.grid(column=1, row=4)
    valor5.focus()
    
    lb6 = Label(window, text="Intervalo Maximo de 'Y': ")
    lb6.grid(column=0, row=5)
    valor6 = Entry(window,width=10)
    valor6.grid(column=1, row=5)
    valor6.focus()
    #PM
    lb7 = Label(window, text="Probabilidad de mutacion del individuo: ")
    lb7.grid(column=0, row=6)
    valor7 = Entry(window,width=10)
    valor7.grid(column=1, row=6)
    valor7.focus()
    
    lb8 = Label(window, text="Probabilidad de mutacion de gen: ")
    lb8.grid(column=0, row=7)
    valor8 = Entry(window,width=10)
    valor8.grid(column=1, row=7)
    valor8.focus()
    #EP
    lb9 = Label(window, text="Resolucion: ")
    lb9.grid(column=0, row=8)
    valor9 = Entry(window,width=10)
    valor9.grid(column=1, row=8)
    valor9.focus()
    
    def valores():
        poblacionI = valor1.get()
        poblacionM = valor2.get()
        minimoX = valor3.get()
        maximoX = valor4.get()
        minimoY = valor5.get()
        maximoY = valor6.get()
        probabilidadM = valor7.get()
        probabilidadG = valor8.get()
        resolucion = valor9.get()
        valorgene = valor10.get()

        poblacionI = int(poblacionI)
        poblacionM = int(poblacionM)
        minimoX = int(minimoX)
        maximoX = int(maximoX)
        minimoY = int(minimoY)
        maximoY = int(maximoY)
        probabilidadM = float(probabilidadM)
        probabilidadG = float(probabilidadG)
        resolucion = float(resolucion)
        valorgene = int(valorgene)
        
        valoresG(poblacionI, poblacionM, minimoX, maximoX, minimoY, maximoY, probabilidadM, probabilidadG, resolucion, valorgene)
    
        
    btn = Button(window, text="Graficar Evolucion", bg="red",fg="white", command=valores)
    btn.grid(column=3, row=10)
    window.mainloop()
    
   
        
        
        
if __name__ == '__main__':
    inicio()
    
    
    










import math
import random  
import string

from individuo import Ind


#Definicion de parametros
#x**2+2*x+3
#Simbolos validos para funcion: +,-,*,/,**,(,)
InitialPopulation = 6
MaxPopulation = 10
ProbMutation = 0.1
ProbMutationGen = 0.05
numGeneration = 5

interval = {
    'x':[-3,4],
    'y':[-1,5]
}

resolution = 0.05

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

Generations = {}
Population = []

def generatePopulation():
    lengthIntervalX = interval['x'][1] - interval['x'][0]
    lengthValuesX= (lengthIntervalX/resolution)+1
    
    lengthIntervalY = interval['y'][1] - interval['y'][0]
    lengthValuesY= (lengthIntervalY/resolution)+1

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
                  
    return [numBitsX,numBitsY]


def mating(numB):

    pTemp = Population

    parents = []

    #Generamos parejas de 2 o 1 aleatoriamente

    while len(pTemp) != 0:
        partner1 = pTemp.pop(random.randint(0,len(pTemp)-1))

        if len(pTemp) != 0:
            partner2 = pTemp.pop(random.randint(0,len(pTemp)-1))
            parents.append([partner1,partner2])
        else:
            parents.append([partner1])

    #Generar la cruza
    children = cruza(parents,numB)

def cruza (parents,numB):

    for i in range( len(parents)):
        spotCruzaX =  random.randint(1,len(parents[i][0].bits['x'])-1)
        spotCruzaY = random.randint(1,len(parents[i][0].bits['y'])-1)
        print(f'Punto de cruza en X {spotCruzaX} pareja {i}')
        print(f'Punto de cruza en Y {spotCruzaY} pareja {i}')

        name1 = ''
        name2 = ''
        if len(parents[i]) !=1:

            p1 = parents[i][0].bits
            p2 = parents[i][1].bits

            print(f'Padre 1 {p1}')
            print(f'Padre 2 {p2}')

            # name1 = name1 + parents[i][0].id + parents[i][1].id


            child1BitsX = []
            child1BitsY = []

            for x in range(len(p1['x'])):

                if x >= spotCruzaX:
                    child1BitsX.append(p2['x'][x])
                else:
                    child1BitsX.append(p1['x'][x])
                    
            for y in range(len(p1['y'])):

                if y >= spotCruzaX:
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

                if y >= spotCruzaX:
                    child2BitsY.append(p1['y'][y])
                else:
                    child2BitsY.append(p2['y'][y])

            child2Bits ={
                'x':child2BitsX,
                'y':child2BitsY
                }

            print(f'Hijo 1 : {child1Bits}')
            print(f'Hijo 2 :{child2Bits}')
            
            #Ahora vemos cual de los hijos mutara o no

            pMCh1 = round(random.uniform(0,1),2)
            pMCh2 = round(random.uniform(0,1),2)
            
            print(f'Probabilidad de Mutacion H1 {pMCh1}')
            print(f'Probabilidad de Mutacion H2 {pMCh2}')
            if pMCh1 <= ProbMutation:
                #Mutara el hijo 1
                #Generar probabilidades de mutacion por gen             

                for i in range(len(p1['x'])):
                    pMGx = round(random.uniform(0,1),3)
                    # print(f'Probabilidad de mutacion GenX {pMGx} Posicion: {i}')
                    if pMGx <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        print(f'Muto el hijo 1 pos {i} X')
                        if child1Bits['x'][i] == 0:
                            child1Bits['x'][i] = 1
                        elif child1Bits['x'][i] == 1:
                            child1Bits['x'][i] = 0

                for i in range(len(p1['y'])):
                    pMGy = round(random.uniform(0,1),3)
                    # print(f'Probabilidad de mutacion GenY {pMGy} Posicion: {i}')
                    if pMGy <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        print(f'Muto el hijo 1 pos {i} Y')
                        if child1Bits['y'][i] == 0:
                            child1Bits['y'][i] = 1
                        elif child1Bits['y'][i] == 1:
                            child1Bits['y'][i] = 0
            

            if pMCh2 <= ProbMutation:
                #Mutara el hijo 1
                #Generar probabilidades de mutacion por gen             

                for i in range(len(p1['x'])):
                    pMGx = round(random.uniform(0,1),3)
                    # print(f'Probabilidad de mutacion GenX {pMGx} Posicion: {i}')
                    if pMGx <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        print(f'Muto el hijo 2 pos {i} X')
                        if child2Bits['x'][i] == 0:
                            child2Bits['x'][i] = 1
                        elif child2Bits['x'][i] == 1:
                            child2Bits['x'][i] = 0

                for i in range(len(p1['y'])):
                    pMGy = round(random.uniform(0,1),3)
                    # print(f'Probabilidad de mutacion GenY {pMGy} Posicion: {i}')
                    if pMGy <= ProbMutationGen:
                        #Va a mutar en esta posicion
                        print(f'Muto el hijo 2 pos {i} Y')
                        if child2Bits['y'][i] == 0:
                            child2Bits['y'][i] = 1
                        elif child2Bits['y'][i] == 1:
                            child2Bits['y'][i] = 0
            
            print(f'Hijo 1 MUTADO: {child1Bits}')
            print(f'Hijo 2 MUTADO: {child2Bits}')

            #Crear el objeto Ind pero como Hijo
            ###################################






        else:
            name=name + parents[i][0].id + parents[i][0].id



        
    return []

if __name__ == '__main__':
    # for i in range(numGeneration):
    #     Generations.update({f'gen{i}':[]})

    
    numB = generatePopulation()
    

    # print(Population)

    mating(numB)
   

    










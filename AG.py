import math
import random  
import string

from individuo import Ind


#Definicion de parametros
#x**2+2*x+3
#Simbolos validos para funcion: +,-,*,/,**,(,)
InitialPopulation = 5
MaxPopulation = 10
ProbMutation = 0.1
ProbMutationGen = 0.05
numGeneration = 10

Generations = {}
Population:Ind = []

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
    # print(aptitudes)

    for i in range(numEliminations):
        # print(f'Minimo: {min(aptitudes)}')
        for x in range(len(aptitudes)):

            if aptitudes[x] == min(aptitudes):
                Population.pop(x)
                aptitudes.pop(x)
                break
    


    # print(aptitudes)


if __name__ == '__main__':

    for i in range(numGeneration):
        Generations.update({f'gen{i+1}':[]})

    # print(Generations)  
    numB = generatePopulation()


    for i in range(numGeneration):

        # print(f'Antes de cruza {len(Population)}')
        mating(numB,numB[2],numB[3])
        
        
        
        # print(f'Antes de poda {len(Population)}')
        if len(Population) > MaxPopulation:
            
            #Inicia poda
            poda()

        # print(len(Population))

        print(f'ES LA GENERACION {i+1}')
        for y in range(len(Population)):
            print(Population[y].toString())

        for x in range(len(Population)):
            Generations[f'gen{i+1}'].append(Population[x])

    # print(Generations)

    
        
    # for i in range(numGeneration):
        # print(Generations[f'gen{i}'])
    print('ESTA ES LA GENERACION 10')
    for i in range(len(Generations['gen10'])):
        print(Generations['gen10'][i].toString())

    print('ESTA ES LA GENERACION 1')
    for i in range(len(Generations['gen1'])):
        print(Generations['gen1'][i].toString())
    # for i in range(len(Generations['gen1'])):
    #     print('GENERACION PRIMERA')
    #     print(Generations['gen1'][i].toString())
        # print(Generations['gen9'][i].aptitude)
    # print(Generations)
   

    










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

    while len(pTemp) != 0:
        partner1 = pTemp.pop(random.randint(0,len(pTemp)-1))

        if len(pTemp) != 0:
            partner2 = pTemp.pop(random.randint(0,len(pTemp)-1))
            parents.append([partner1,partner2])
        else:
            parents.append([partner1])

    children = cruza(parents,numB)

def cruza (parents,numB):

    for i in range( len(parents)):
        spotCruzaX =  random.randint(1,len(parents[i][0].bits['x'])-1)
        spotCruzaY = random.randint(1,len(parents[i][0].bits['y'])-1)
        print(f'Punto de cruza en X {spotCruzaX} pareja {i}')
        print(f'Punto de cruza en Y {spotCruzaY} pareja {i}')

        name = ''
        if len(parents[i]) !=1:

            p1 = parents[i][0].bits
            p2 = parents[i][1].bits

            print(f'Padre 1 {p1}')
            print(f'Padre 2 {p2}')

            name1 = name1 + parents[i][0].id + parents[i][1].id
            child1 = Ind(numB,[interval['x'][0],interval['y'][0]],resolution,name1)

            child1BitsX = []
            child1BitsY = []
            for x in range(len(p1['x'])):

                if x >= spotCruzaX:
                    child1BitsX.append(p2.bits['x'][x])
                else:
                    child1BitsX.append(p1.bits['x'][x])

            print(f'Bits del hijo cruzado en X {child1BitsX}')

            child2 = Ind(numB,[interval['x'][0],interval['y'][0]],resolution,name)




        else:
            name=name + parents[i][0].id + parents[i][0].id



        
    return []

if __name__ == '__main__':

    # for i in range(numGeneration):
    #     Generations.update({f'gen{i}':[]})

    
    numB = generatePopulation()

    # mating(numB)

    










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

    #Verificar el numero de bits de X y Y
    numBitsX = 1
    numBitsY = 1
    
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
    
        print(ind.toString())
             

    
    
        

if __name__ == '__main__':
    # for i in range(numGeneration):
    #     Generations.update({f'gen{i}':[]})

    
    generatePopulation()









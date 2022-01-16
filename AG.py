import math
import random  
import string



#Definicion de parametros
#x**2+2*x+3
#Simbolos validos para funcion: +,-,*,/,**,(,)
InitialPopulation = 2
MaxPopulation = 10
ProbMutation = 0.1
ProbMutationGen = 0.05
fx ='x^2+3x'
interval =[-3,4]
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

def evaluateFunction(function:str,x):

    y = eval(function,{
    'x':x
    })

    return y

class Ind:
    def __init__(self,noBits):
        # print('a')
        self.genenerateData(noBits)
    
    def genenerateData(self,noBits):
        #Generar id al azar
        self.id = str(chr(random.randint(ord('A'), ord('Z'))))+str()

        #Generar bits dependiendo del numero proporcionado
        self.bits = []

        for i in range(noBits):
            self.bits.append(round(random.random()))
        self.bitsStr = ''
        for i in range(len(self.bits)):
            self.bitsStr += str(self.bits[i])

        #Generar el numero bit-decimal
        position = len(self.bits)-1
        self.decimal = 0

        for i in range(len(self.bits)):
            currentBit = self.bits[i]
            if currentBit == 1:
                self.decimal += 2**position
            position -= 1
        #Generar fenotipo
        self.fenotipe = round((interval[0]+self.decimal)*resolution,3)

        #Generar aptitud de el individuo
        self.aptitude = round(evaluateFunction(transform(fx),self.fenotipe),3)
    
    def toString(self):
        print('___________________________')
        print('id: '+self.id)
        print('Bits: '+str(self.bits))
        print('Decimal: '+str(self.decimal))
        print('Fenotipo: '+str(self.fenotipe))
        print('Aptitud: '+str(self.aptitude))
        print('___________________________')
        

Population:Ind = []
def generatePopulation():
    lengthInterval = interval[1] - interval[0]

    lengthValues = (lengthInterval/resolution)+1

    #Verificar el numero de bits
    numBits = 1
    while(True):
        if lengthValues <= 2**numBits:
            break
        numBits = numBits + 1

    #Generamos los individuos con la clase Ind
    for i in range(InitialPopulation):
        ind1 = Ind(numBits)
        Population.append(ind1)
    
    for i in range(len(Population)):
        Population[i].toString()

    
    
    



    
             

    
    
        

if __name__ == '__main__':
    # print('hola')

    # ind1= Ind(10)

    generatePopulation()









# evaluateFunction(transform(fx),2)





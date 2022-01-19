import random 

Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class Ind:
    def __init__(self,noBits, intervaloA, resolucion,idParents):
        
        
        self.genenerateData(noBits,intervaloA,resolucion,idParents)
        
    
    def genenerateData(self,noBits,intervaloA,resolucion,idParents):
        #Generar id al azar
        self.id = Letters.pop()

        if idParents != None:
            self.id= idParents

        #Generar bits dependiendo del numero proporcionado
        self.bits = {
            'x':[],
            'y':[]
        }

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
        self.fenotipe = round((intervaloA + self.decimal)* resolucion,3)

        #Generar aptitud de el individuo
        #self.aptitude = round(evaluateFunction(transform(fx),self.fenotipe),3)

    def evaluateFunction(self,function:str,x,y):

        z = eval(function,{
        'x':x,
        'y':y
        })

        return z
    
    def toString(self):
        print('___________________________')
        print('id: '+self.id)
        print('Bits: '+str(self.bits))
        print('Decimal: '+str(self.decimal))
        print('Fenotipo: '+str(self.fenotipe))
        print('Aptitud: '+str(self.aptitude))
        print('___________________________')
        
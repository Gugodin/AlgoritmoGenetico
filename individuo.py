import random 

Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
fx ='-x**3+4*x*y-2*y**2+1'
class Ind:
    def __init__(self,noBits, intervaloA, resolucion,idParents, bits = {}):      
        if idParents == None:
            self.genenerateDataInd(noBits,intervaloA,resolucion)
        else:
            self.generateDataChild(idParents,bits)

    def generateDataChild(self,idParents,bits):

        self.id = idParents

        self.bits = bits

        


        print()
        
    def genenerateDataInd(self,noBits,intervaloA,resolucion):
        #Generar id al azar
        self.id = Letters.pop()

        #Generar bit y decimal
        self.generateBits(noBits)

        #Generar fenotipo
        self.generateFenotipe(intervaloA,resolucion)

        #Generar aptitud de el individuo
        self.aptitude = round(self.evaluateFunction(fx,self.fenotipe['x'],self.fenotipe['y']),3)
        
    def generateFenotipe(self,intervaloA,resolucion):

        self.fenotipe = {
            'x':0,
            'y' :0
        }
        
        self.fenotipe['x'] = round(intervaloA[0] + self.decimal['x'] * resolucion,3)
        self.fenotipe['y'] = round(intervaloA[1] + self.decimal['y'] * resolucion,3)


    def evaluateFunction(self,fx:str,x,y):

        z = eval(fx,{
        'x':x,
        'y':y
        })

        return z

    def generateBits(self, noBits):
        #Generar bits dependiendo del numero proporcionado
        
        self.bits = {
            'x':[],
            'y':[]
        }

        for i in range(noBits[0]):
            self.bits['x'].append(round(random.random()))
       
        for i in range(noBits[1]):
            self.bits['y'].append(round(random.random()))

        #Generar el numero bit-decimal
        
        positionX = len(self.bits['x'])-1
        positionY = len(self.bits['y'])-1

        self.decimal = {
            'x':0,
            'y':0
        }

        for i in range(len(self.bits['x'])):
            currentBit = self.bits['x'][i]
            if currentBit == 1:
                self.decimal['x'] += 2**positionX
            positionX -= 1
            
        for i in range(len(self.bits['y'])):
            currentBit = self.bits['y'][i]
            if currentBit == 1:
                self.decimal['y'] += 2**positionY
            positionY -= 1

    # APAREAMIENTO Y CRUZA
    
    
    def toString(self):
        return f'id: {self.id}\n' + f'Bits: {str(self.bits)}\n' + f'Decimal: {str(self.decimal)}\n' + f'Fenotipo: {str(self.fenotipe)}\n' + f'Aptitud: {str(self.aptitude)}\n'
        
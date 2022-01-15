import math 



#Definicion de parametros
#x**2+2*x+3
#Simbolos validos para funcion: +,-,*,/,**,(,)
exp= 'x**2+2*x*(3)'
x1 = 2
y = eval(exp,{
    'x':x1
})

# print(str(y)) 




fx ='x^2+(2x+3x(4x))'

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

    print(y)





evaluateFunction(transform(fx),2)





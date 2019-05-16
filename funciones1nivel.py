def normal(x):
    return x

def cuadrado(x):
    return x*x

def sumaTodos(limitTo, f): #f contendra la referencia a la funcion que queremos hacer
    resultado = 0
    for i in range (limitTo+1):
        resultado += f(i)
        
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))
import math

def calcularInteres(precio, interes):

    return precio * interes

def calcularPrecio(precio, ganancia):
    
    return precio + (ganancia * precio )

def precioVenta(precio, interes,ganancia):
    total = calcularPrecio(precio, ganancia)
    interes = calcularInteres(total,interes)
    return total + interes

interes = float(input("ingrese el interes"))
precio = float(input("Ingrese el precio"))
ganancia =float(input("Ingrese la ganacia"))

print(precioVenta(precio, interes, ganancia ))

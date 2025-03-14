def calculadora():
    print("Calculadora Básica")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Intente de nuevo.")

calculadora()

import random

def numero_aleatorio():
    print("Generador de Número Aleatorio")
    num = random.randint(1, 100)
    print(f"Número generado: {num}")

numero_aleatorio()

def comparar_cadenas():
    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    
    if cadena1 == cadena2:
        print("Las cadenas son iguales.")
    else:
        print("Las cadenas son diferentes.")
        if cadena1 > cadena2:
            print(f'"{cadena1}" es mayor en orden alfabético que "{cadena2}".')
        else:
            print(f'"{cadena2}" es mayor en orden alfabético que "{cadena1}".')

comparar_cadenas()

print("Bienvenido dinos los precio, ganncia y impuesto")
#escribir  leer 
precio =  input("engrese el precio: ")
precio = float(precio)
ganacia =  input("engrese el ganancia: ")
ganacia = float(ganacia)
impuesto =  input("engrese el impuesto: ")
impuesto = float(impuesto)
#funcion nombre de l avariable()
def calcularImpuesto(impuesto, precio):
    return impuesto * precio
def calcularGanancia(ganacia, precio):
    return ganacia * precio

def calcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = calcularGanancia(ganacia, precio) + precio
    impuestVenta = calcularImpuesto(impuesto, precio1)
    return precio1 + impuestVenta

print(calcularPrecioFinal(precio, impuesto, ganacia))
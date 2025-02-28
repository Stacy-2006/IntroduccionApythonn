numero = input("Ingrese un numero")
if numero.isdigit():
    suma= 0 
    for digito in numero: 
        suma += int(digito)
        print(f"La suma de los diguitos de {numero} es {suma}")
else:
    print("por favor, ingrese un número válido.")
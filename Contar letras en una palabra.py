palabra = input("Ingrese una palabra: ")
contador = 0

for letra in palabra:
    if letra.isalpha():  
        contador += 1

print(f'La palabra "{palabra}" tiene {contador} letras.')
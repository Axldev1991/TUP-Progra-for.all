#7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

positivos = 0
negativos = 1
i = 0

while True:
    numero = input("Ingrese un número (para finalizar presione 'n'): ")

    if numero == "n":
        break
    
    numero = int(numero)

    if numero >= 0:
        positivos += numero

    else:
        negativos *= numero
        i = 1

suma = positivos

if i == 0:
    negativos = 0

print(f"La suma de los numeros positivos es: {positivos}")
print(f"EL producto de los numeros negativos es: {negativos}")

# https://onlinegdb.com/na2Aba0b7
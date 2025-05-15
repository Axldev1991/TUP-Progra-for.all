#9 Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

i = 0
suma = 0
continuar = "si"

while continuar == "si":
    if i < 5:
        numero = int(input("Ingrese un número: "))
        suma += numero

    else:
        continuar = input("¿Desea continuar? si/no: ")

        if continuar == "no":
            break

        numero = int(input("Ingrese un número: "))
        suma += numero

    i += 1

promedio = suma / i
print(f"La suma total de los números ingresados es: {suma}")
print(f"EL promedio de la suma de los números es: {promedio}")

# https://onlinegdb.com/vVdWNt5XD
#6 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

i = 0
suma = 0

while True:
    numero = input("Ingrese un número (para finalizar presione 'n'): ")

    if numero == "n":
        break
    
    suma += int(numero)
    i += 1

promedio = suma / i
print(f"La suma total de los números ingresados es: {suma}")
print(f"EL promedio de la suma de los números es: {promedio}")

# https://onlinegdb.com/yO52LcRsZ
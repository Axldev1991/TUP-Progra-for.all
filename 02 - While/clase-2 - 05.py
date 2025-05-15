#5 Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

i = 0
suma = 0

while i < 5:
    numero = int(input("Ingrese un número: "))
    suma += numero
    i += 1

promedio = suma / i
print(f"La suma total de los números ingresados es: {suma}")
print(f"EL promedio de la suma de los números es: {promedio}")

# https://onlinegdb.com/Y_7rnpRf4
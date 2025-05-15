# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
    # La suma acumulada de los números negativos.
    # La suma acumulada de los números positivos.
    # La cantidad de números negativos ingresados.
    # El promedio de los números positivos.
    # El número positivo más grande.
    # El porcentaje de números negativos ingresados, respecto del total de ingresos.


i = 0
suma_positivos = 0
suma_negativos = 0
cantidad_positivos = 0
cantidad_negativos = 0
maximo = 0
continuar = "si"

while continuar == "si":
    numero = int(input("Ingrese un numero: "))

    if numero >= 0:
        suma_positivos += numero
        cantidad_positivos += 1

        if numero > maximo:
            maximo = numero

    else:
        suma_negativos += numero
        cantidad_negativos += 1

    continuar = input("¿desea continuar? si/no: ")

    i += 1

if cantidad_positivos > 0:
    promedio = suma_positivos / cantidad_positivos
else:
    promedio = 0
    maximo = "No existe un máximo positivo debido a que no se ingresó ningún número positivo"
    
porcentaje_negativos = cantidad_negativos / i * 100

print(f"La suma total de los números negativos: {suma_negativos}")
print(f"La suma total de los números positivos: {suma_positivos}")
print(f"La cantidad de los números negativos ingresados es: {cantidad_negativos}")
print(f"EL promedio de los numeros positivos es: {promedio}")
print(f"EL maximo número positivo es: {maximo}")
print(f"EL porcentaje de numeros negativos ingresados es: %{porcentaje_negativos}")

# https://onlinegdb.com/MSawl9t-H7x
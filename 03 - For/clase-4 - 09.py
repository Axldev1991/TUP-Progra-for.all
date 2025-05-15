#9 Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
    
    if numero % i == 0:
        print(f"{i} es dividor de {numero}")

# https://onlinegdb.com/KqSFmIDei
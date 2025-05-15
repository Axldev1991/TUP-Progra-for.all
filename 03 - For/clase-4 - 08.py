#8 Realizar un programa que permita mostrar una pirámide de números

numero = int(input("Ingrese un número: "))
acumulador = ""

for i in range(1, numero + 1):
    
    acumulador += str(i)
    print(acumulador)

# https://onlinegdb.com/hDaoN9PjC
#8 Ingresar 10 números enteros. Determinar el máximo y el mínimo.

i = 0
maximo = 0
minimo = 0

while i < 10:
    numero = int(input("Ingrese un número: "))

    if numero > maximo or i == 0:
        maximo = numero

    if numero < minimo or i == 0:
        minimo = numero

    i += 1

print(f"El máximo número es: {maximo}")
print(f"El mínimo número es: {minimo}")

# https://onlinegdb.com/_1yFLZ1UD2

# maximo = float("-inf")
# minimo = float("inf")


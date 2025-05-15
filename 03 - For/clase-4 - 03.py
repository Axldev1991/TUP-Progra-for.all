#3 Ingresar un número. Mostrar los números desde 0 hasta el número ingresado

numero = int(input("Ingrese un número mayor a 0: "))

while numero < 0:
    numero = int(input("Error...Ingrese un número mayor a 0: "))

for i in range(0, numero+1):
    print(i, end = "-")

# https://onlinegdb.com/-0jJbyAwC
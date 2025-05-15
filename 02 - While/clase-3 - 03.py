#3 Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota = int(input("Ingrese una nota: "))

while nota < 1 or nota >10:

    print("Error, la nota está por fuera de los límites")
    nota = int(input("Ingrese una nota: "))


print("Fin del programa")

# https://onlinegdb.com/Xvc3RHmoS

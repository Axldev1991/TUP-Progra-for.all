#6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par(numero):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

numero = 11
verificar = verificar_par(numero)

# https://onlinegdb.com/xUJ5KMpLv
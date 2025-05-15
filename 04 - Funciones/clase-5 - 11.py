#11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

""" def encontrar_primo(numero):
    contador = 0

    for i in range(1, numero+1):    
        bandera_divisor = False
        
        for j in range(2, i):
            if i % j == 0:
                bandera_divisor = True

        if bandera_divisor == True:        
            continue

        else:
            contador += 1
    return contador """

def es_primo(i):
    bandera = True
    for j in range(2, i):
        if i % j == 0:
            bandera = False
            break
    return bandera

def mostrar_primo(numero):
    contador = 0

    for i in range(2, numero+1):    
        divisor = es_primo(i)

        if divisor == False:        
            continue

        else:
            contador += 1
    return contador

numero = 13
numero_analizado = mostrar_primo(numero)
print(numero_analizado)


# https://onlinegdb.com/6NSDGtUdq



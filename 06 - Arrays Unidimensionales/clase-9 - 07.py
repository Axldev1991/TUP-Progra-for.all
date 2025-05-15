#7 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

lista = [-2, -3, 1, -6, 9, -10, 9, 9]

def calcular_maximo_lista(vector):
    maximo = vector[0]
    posiciones = [0]

    for i in range(1, len(vector)):
        if vector[i] > maximo:
            maximo = vector[i]
            posiciones = [i]
        elif vector[i] == maximo:
            posiciones += [i]

    return posiciones

print(f"El máximo valor de la lista se encuentra en las posiciones: {calcular_maximo_lista(lista)}")



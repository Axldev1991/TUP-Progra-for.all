#7 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

# lista = [-2, -3, 1, -6, 9, -10, 9, 9]


lista = [-10, 40, -11 , -5, 20,  -250, 20, 7, 11, 1, 40]


def calcular_maximo_lista(vector):
    maximo = 0
    posiciones = []

    for i in range(len(vector)):
        if vector[i] > maximo or i == 0:
            maximo = vector[i]
            posiciones = [i]
        elif vector[i] == maximo:
            posiciones += [i]        

    return posiciones

print(f"El máximo valor de la lista se encuentra en las posiciones: {calcular_maximo_lista(lista)}")



#6 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

lista = [-2, -3, 1, -6, 9, -10, -5]

def calcular_maximo_lista (vector: int):
    maximo = 0
    posicion_maximo = 0
    for i in range(len(vector)):
        if vector[i] > maximo or i == 0:
            posicion_maximo = i
    return posicion_maximo

print(f"El máximo valor de la lista se encuentra en la posición: {calcular_maximo_lista(lista)}")


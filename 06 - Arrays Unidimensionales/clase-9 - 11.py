#11 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.

lista_1 = [-2, -3, 1, -6, 9, -10, 10]
lista_2 = [2, 3, 1, -6, -9, 10, 9, -2]

def calcular_diferencia (vector_1: list, vector_2: list) -> list:
    lista_diferencia = []
    
    for i in range(len(vector_1)):
        bandera_repetidos = False
        for j in range(len(vector_2)):
            if vector_1[i] == vector_2[j]:
                bandera_repetidos = True
        if bandera_repetidos == False:
            lista_diferencia += [vector_1[i]]
        
    print(lista_diferencia)

calcular_diferencia(lista_1, lista_2)
calcular_diferencia(lista_2, lista_1)




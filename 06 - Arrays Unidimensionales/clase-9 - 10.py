#10 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

lista_1 = [-2, -3, 1, -6, 9, -10, 10]
lista_2 = [2, 3, 1, -6, -9, 10, 9, -2]

def calcular_union (vector_1: list, vector_2: list) -> list:
    lista_union = lista_1
    # for i in range(len(vector_1)):
    #     bandera_repetidos = False
    #     for j in range(len(lista_union)):
    #         if vector_1[i] == lista_union[j]:
    #             bandera_repetidos = True
    #     if bandera_repetidos == False:
    #         lista_union += [vector_1[i]]
    
    for i in range(len(vector_2)):
        bandera_repetidos = False
        for j in range(len(lista_union)):
            if vector_2[i] == lista_union[j]:
                bandera_repetidos = True
        if bandera_repetidos == False:
            lista_union += [vector_2[i]]
    print(lista_union)

calcular_union(lista_1, lista_2)
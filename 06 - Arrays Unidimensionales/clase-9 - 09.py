#9 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

lista_1 = [-2, -3, 1, -6, 9, -10, 10]
lista_2 = [2, 3, 1, -6, -9, 10, -9, 9, -2]

# def calcular_intersección (vector_1: list, vector_2: list) -> list:
#     interseccion_listas = []
#     for i in range(len(vector_1)):
#         for j in range(len(vector_2)):
#             if vector_1[i] == vector_2[j]:
#                 ya_esta = False
#                 for k in range(len(interseccion_listas)):
#                     if vector_1[i] == interseccion_listas[k]:
#                         ya_esta = True
#                 if ya_esta == False:
#                     interseccion_listas += [vector_1[i]]                
#     return interseccion_listas

def calcular_intersección (vector_1: list, vector_2: list) -> list:
    lista_interseccion = []
    for i in range(len(vector_1)):
        for j in range(len(vector_2)):
            if vector_1[i] == vector_2[j]:
                lista_interseccion += [vector_1[i]]
                break
    print(lista_interseccion)

calcular_intersección(lista_1, lista_2)
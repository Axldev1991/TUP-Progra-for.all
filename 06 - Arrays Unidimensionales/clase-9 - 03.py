#3 Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

lista = [2, 3, 1, 6, 9]

def calcular_promedio_lista (vector: int):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]

    promedio = suma / len(vector)
    print(f"El prmedio de la lista es: {promedio}")

calcular_promedio_lista(lista)


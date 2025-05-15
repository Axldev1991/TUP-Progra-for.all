#4 Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. 

lista = [-2, -3, 1, -6, 9, -10, -5]

def calcular_promedio_lista_positivos (vector: int):
    suma = 0
    contador = 0
    for i in range(len(vector)):
        if vector[i] > 0:
            suma += vector[i]
            contador += 1
    if contador > 0:
        promedio = suma / contador
    else:
        promedio = "Error de cálculos"
    print(f"El prmedio de la lista es: {promedio}")

calcular_promedio_lista_positivos(lista)


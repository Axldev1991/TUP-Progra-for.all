#5 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

lista = [-2, -3, 1, -6, 9, -10, -5]

def calcular_producto_lista (vector: int):
    producto = 1
    for i in range(len(vector)):
        producto *= vector[i]
    return producto

print(calcular_producto_lista(lista))


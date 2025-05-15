#2 Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

def crear_array (cantidad_elementos: int) -> int:
    vector = [None] * cantidad_elementos
    return vector

def pedir_cantidad_numeros (cantidad_numeros_vector: int):
    vector = crear_array(cantidad_numeros_vector)
    for i in range(cantidad_numeros_vector):
        vector[i] = int(input(f"Ingrese el número en la posición {i+1}: "))
    return vector

q = int(input("Que cantidad de números desea cargar?: "))
x = pedir_cantidad_numeros(q)
print(x)

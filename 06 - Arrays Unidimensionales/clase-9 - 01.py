#1 Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array (cantidad_elementos: int) -> list:
    vector = [None] * cantidad_elementos
    return vector

longitud_vector = int(input("Ingrese la longitud del vector: "))
vector = crear_array(longitud_vector)
print(len(vector))


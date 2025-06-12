# Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera ocurrencia de dicho caracter, o -1 en caso de que no esté.

cadena = "oihasdhs"

def buscar_indice(cadena: str, caracter: str) -> int:
    indice = 0
    for i in range(len(cadena)):
        if caracter == cadena[i]:
            indice = i
            break
    if indice == 0:
        indice = -1
    return indice

x = buscar_indice(cadena, "s")
print(x)

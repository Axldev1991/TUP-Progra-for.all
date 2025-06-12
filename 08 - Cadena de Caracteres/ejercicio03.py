# Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.

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

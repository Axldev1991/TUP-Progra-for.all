# Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.

cadena = "oihasdhs"

def eliminar_repetido(cadena: str):
    nueva_cadena = ""
    for i in range(len(cadena)):
        if cadena[i] == cadena[i-1]:
            continue
        nueva_cadena += cadena[i]
    return nueva_cadena

x = eliminar_repetido("aaaaaahhhhh        uuuuuuuqwertyu")
print(x)
# Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.



def eliminar_vocales(cadena: str):
    vocales = "aeiou"
    nueva_cadena = ""
    for i in range(len(cadena)):
        es_vocal = False
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                es_vocal = True
                break
        if es_vocal == False:
            nueva_cadena += cadena[i]
    return nueva_cadena

x = eliminar_vocales("sasesisosuaeiuopyyywtwtwtwte")
print(x)
# Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

# def contar_subcadena(cadena: str, subcadena: str):
#     contador = 0
#     i = 0
#     while i <= len(cadena) - len(subcadena):
#         coincide = True
#         for j in range(len(subcadena)):
#             if cadena[i+j] != subcadena[j]:
#                 coincide = False
#                 break
#         if coincide:
#             contador += 1
#             i += len(subcadena)
#         else:
#             i += 1
#     return contador

def contar_subcadena(cadena: str, subcadena: str):
    contador = 0

    for i in range(len(cadena)):
        if cadena[i] == subcadena[0]:
            nueva_cadena = ""

            for j in range(len(subcadena)):
                nueva_cadena += cadena[i+j]

            if nueva_cadena == subcadena:
                contador += 1
    print(contador)


contar_subcadena("El pan del panaderopanpanpanpanasd", "pan")

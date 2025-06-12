from Sospechosos import *

muestra_del_crimen = "CGTTTAATG"


def contar_subcadena(cadena: str, subcadena: str):
    contador = 0

    for i in range(len(cadena)):
        if cadena[i] == subcadena[0]:
            nueva_cadena = ""

            if (i + len(subcadena)) > len(cadena):
                break
            else:
                for j in range(len(subcadena)):
                    nueva_cadena += cadena[i+j]

                if nueva_cadena == subcadena:
                    contador += 1
    return contador

indice_sospechosos = []
for i in range(len(muestras)):
    coincidencia = contar_subcadena(muestras[i], muestra_del_crimen)
    if coincidencia > 0:
        indice_sospechosos += [i]
        print(i)
print(indice_sospechosos)

print(f"Los sospechosos del crimen son: ")
for i in range(len(indice_sospechosos)):
    print(sospechosos[indice_sospechosos[i]])


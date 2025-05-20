import sys
import random
from os import system
from validate import *
from input import *
from array_generales import *

def main():
    print("Bienvenido usuario! Siéntese cómodo y dígame usted, que desea hacer?")
    opcion = solicitar_entero("Opcion (1): Cargar matriz manualmente.\nOpción (2): cargar matriz automáticamente.\nOpción (3): Generar cuadrado mágico.\n", "Error, lea bien las opciones!!: ", 1, 3)

    rango = solicitar_entero("Que Rango debería tener la matriz?: ", "Error, el rango debe ser mayor a 3", 3, 5)

    constante_magica = calcular_contante_magica(rango, rango)

    match opcion:
        case 1:
            matriz = crear_matriz(rango, rango)
            cargar_matriz(matriz, f"Ingrese el valor en la posicion : ", f"Error, el N° ya fué ingresado o está fuera del rango (1 - {rango**2}): ", rango, False )
            print("\nUsted ingresó la siguiente matriz: ")
            mostrar_formato_matriz(matriz)
            print("Verifiquemos su poder mágico...")
            verificador = verificar_cubo_magico(matriz, constante_magica)
            system("pause")
            system("cls")
            if verificador:
                print("BRAVO! SU CUADRADO ES MÁGICO")
            else:
                print("Lamento decirle... su cuadrado no es más que eso...")
            mostrar_formato_matriz(matriz)
        case 2:
            matriz = crear_matriz(rango, rango)
            cargar_matriz(matriz, "", "", rango, True)
            print("\nHemos creado para usted la siguiente matriz: ")
            mostrar_formato_matriz(matriz)
            print("Verifiquemos su poder mágico...")
            verificador = verificar_cubo_magico(matriz, constante_magica)
            system("pause")
            system("cls")
            if verificador:
                print("BRAVO! SU CUADRADO ES MÁGICO")
            else:
                print("Lamento decirle... su cuadrado no es más que eso...")
            mostrar_formato_matriz(matriz)
        case 3:
            matriz_magica = crear_matriz(rango, rango, 0)
            matriz_magica = crear_cubo_magico(matriz_magica, constante_magica)
            print("ABRAKADABRA!")
            system("pause")
            system("cls")
            print("Este es un cuadrado mágico")
            mostrar_formato_matriz(matriz_magica)

if __name__ == "__main__":
    sys.exit(main())

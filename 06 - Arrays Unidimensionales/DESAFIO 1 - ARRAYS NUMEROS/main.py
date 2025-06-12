from colorama import init, Fore, Back, Style
init(autoreset=True)
import sys
from os import system

from input import *
from array_generales import *

menu =[
        "(1) Ingresar datos",
        "(2) Mostrar cantidad de positivos y negativos",
        "(3) Sumatoria de números pares",
        "(4) Mostrar mayor números impar",
        "(5) Mostrar números ingresados",
        "(6) Mostrar números pares",
        "(7) Mostrar números en posiciones impares",
        "(8) Salir",
    ]

def main():
    correr_programa = True
    existe_datos = False
    mensaje = "Elija una opción: "
    mensaje_error =  Back.RED + "Error. Elija una opción válida: "
    separador = "----------------------"

    while correr_programa:
        print(separador)
        imprimir_menu(menu)
        print(separador)

        opcion = solicitar_entero(mensaje, mensaje_error, 1, 8)
        # if existe_datos == False:
        #     if opcion == 8:
        #         correr_programa = False
        #     elif opcion != 1:
        #         print(Fore.GREEN + "Primero debe elegir la opcion (1) para poder continuar. ")                
        #         continue
        # else:
        #     if opcion == 1:
        #         print(Fore.BLUE + "Los datos ya fueron ingresados. Elija otra opción.")                
        #         continue

        match opcion:
            case 1:
                datos = ingresar_datos(Fore.GREEN + "Ingrese un número entero: ", Fore.RED +"Error, ingrese un número entre -1000/1000: ", False)
                existe_datos = True
            case 2:
                contador = contar_positivos_negativos(datos)
                print(Back.LIGHTBLUE_EX + f"Cantidad de N° positivos: {contador[0]}")
                print(Back.LIGHTBLUE_EX + f"Cantidad de N° negativos: {contador[1]}")
            case 3:
                sumatoria_pares = sumar_pares(datos)
                print(Back.LIGHTBLUE_EX + f" La sumatoria de los N° pares es: {sumatoria_pares}")
            case 4:
                mayor_impar = buscar_mayor_impar(datos)
                print(Back.LIGHTBLUE_EX + f"El mayor N° impar es: {mayor_impar}")
            case 5:
                mostrar_lista(datos)                
            case 6:
                lista_pares = listar_pares(datos)
                mostrar_lista(lista_pares)
            case 7:
                posiciones_impares = listar_posicion_impar(datos)
                mostrar_lista(posiciones_impares)
            case 8:
                print(Back.RED + "FIN DEL PROGRAMA")
                correr_programa = False
        system("pause")
        system("cls")


if __name__ == "__main__":
    sys.exit(main())





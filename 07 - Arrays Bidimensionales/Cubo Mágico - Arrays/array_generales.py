import random
from validate import *

def crear_matriz(filas: int, columnas: int, contenido: int = 0) ->list:
    """Funcion que permite crear una matriz de determinada cantidad de filas y columnas.

    Args:
        filas (int): Cantidad de filas para crear la matriz.
        columnas (int): Cantidad de columnas para crear la matriz.
        contenido (int, optional): Contenido para volcar en todos los valores de la matriz. Defaults to 0.

    Returns:
        list: Devuelve la matriz.
    """
    matriz = [[contenido] * columnas for _ in range(filas)]    
    return matriz

def mostrar_formato_matriz(matriz: list):
    """Funcion para mostrar una matriz de manera más comprensible para el usuario.

    Args:
        matriz (list): Matriz a mostrar.

    Returns:
        ---
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:>3}", end=" ")
        print("")

def crear_cubo_magico(matriz: list, constante: int) -> list:
    """Funcion para crear de manera automática un cuadrado mágico de orden nxn.

    Args:
        matriz (list): Matriz en la cual crear el cuadrado mágico.
        constante (int): Constante mágica.

    Returns:
        list: Devuelve el cuadrado (matriz) mágica.
    """
    bandera_magica = False
    while bandera_magica == False:
        repetidos = True
        while repetidos:
            lista_usados = []        
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    bandera_verificacion = True                
                    while bandera_verificacion:
                        numero = random.randint(1, (len(matriz))**2)
                        numero_a_verificar = verificar_repetido_lista(lista_usados, numero)

                        if numero_a_verificar == False:
                            matriz[i][j] = numero
                            lista_usados += [numero]
                            bandera_verificacion = False
                        else:
                            continue
                checkfila = verificar_filas_magicas([matriz[i]], constante)
                if checkfila == False:
                    break
            if checkfila:
                repetidos = False
        check = verificar_cubo_magico(matriz, constante)
        if check:
            bandera_magica = True
    return matriz


from especificas import *
from colorama import init, Fore, Back, Style
init(autoreset=True)

def contar_positivos_negativos(vector: list) -> list:
    """Cuenta la cantidad de N° positivos y negativos de una lista.

    Args:
        vector (list): Recibe una lista de números enteros.

    Returns:
        list: Devuelve una lista de longitud 2: lista[0] = Cantidad N° positivos; lista[1] = Cantidad N° negativos
    """
    contador_positivos_negativos = [0] * 2
    for i in range(len(vector)):
        verificar = verificar_positivo(vector[i])
        if verificar:
            contador_positivos_negativos[0] += 1
        else:
            contador_positivos_negativos[1] += 1
    return contador_positivos_negativos

def sumar_pares(vector: list) -> int:
    """Calcula la sumatoria de los números pares en una lista.

    Args:
        vector (list): Recibe una lista con números.

    Returns:
        int: Devuelve la sumatoria de los números.
    """
    sumatoria = 0
    for i in range(len(vector)):
        verificar = verificar_par(vector[i])
        if verificar:
            sumatoria += vector[i]
    return sumatoria

def buscar_mayor_impar(vector: list) -> int:
    """Busca el mayor N° impar en una lista de números.

    Args:
        vector (list): Recibe una lista de números.

    Returns:
        int: Devuelve el mayor N° impar de la lista.
    """
    mayor = vector[0]
    for i in range(len(vector)):
        verificar = verificar_par(vector[i])
        if verificar == False:
            if vector[i] > mayor:
                mayor = vector[i]
    return mayor

def mostrar_lista(vector: list):
    """Imprime en pantalla una lista indicando la posición de cada elemento para el usuario.

    Args:
        vector (list): Recibe una lista a imprimir.
    """
    for i in range(len(vector)):
        print(Back.LIGHTBLUE_EX + f" {i+1}°:  {vector[i]} ", end= " | ")

def listar_pares(vector: list) -> list:
    """Muestra una lista de N° pares, de una lista de N° recibida.

    Args:
        vector (list): Recibe una lista de números.

    Returns:
        list: Devuelve una lista de números pares.
    """
    lista_pares = []
    for i in range(len(vector)):
        verificar = verificar_par(vector[i])
        if verificar:
            lista_pares += [vector[i]]
    return lista_pares

def listar_posicion_impar(vector: list) -> list:
    """Muestra los N° de una lista en las posiciones impares de la lista.

    Args:
        vector (list): Recibe una lista de N°

    Returns:
        list: Devuelve una lista con los N° en las posiciones impares de la lista recibida
    """
    lista = []
    for i in range(1, len(vector), +2):
        lista += [vector[i]]
    return lista

def imprimir_menu(vector: list):
    """Imprime una lista en pantalla. Creada para imprimir un menú de opciones.

    Args:
        vector (list): Recibe una lista con datos a imprimir en pantalla.
    """
    for i in range(len(vector)):
        print(Fore.YELLOW + vector[i])


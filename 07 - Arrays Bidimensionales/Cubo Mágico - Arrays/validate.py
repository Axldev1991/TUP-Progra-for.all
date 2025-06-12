import random

def validar_numero (numero, minimo: int, maximo: int) -> bool:
    """Valida si el ingreso en un INPUT es INT, FLOAT, STR.

    Args:
        numero (_type_): El input a validar.
        minimo (int): Límite inferior a validar el dato.
        maximo (int): Límite superior a validar el dato.

    Returns:
        bool: True = int / False = Float / None = str
    """
    bandera_validacion = None
    if numero.isalpha() == False:
        numero = float(numero)
        if numero >= minimo and numero <= maximo:
            if numero % 1 == 0:
                bandera_validacion = True
            else:
                bandera_validacion = False
        return bandera_validacion

def verificar_repetido_lista(lista: list, numero: int) -> bool:
    """Funcion para verificar si un N° existe en una lista

    Args:
        lista (list): Lista a verificar los datos internos.
        numero (int): Valor a comprobar si existe o no en la lista.

    Returns:
        bool: True = El valor existe en la lista (False caso contrario).
    """
    bandera = False
    for i in range(len(lista)):
        if numero == lista[i]:
            bandera = True
            break
    return bandera

def calcular_contante_magica(cantidad_filas: int, cantidad_columnas: int) -> int:
    """Función para calcular una constante mágica (para el ejercicio del cuadrado mágico).

    Args:
        cantidad_filas (int): Cantidad de filas que contiene la matriz
        cantidad_columnas (int): Cantidad de columnas que contiene la matriz

    Returns:
        int: Valor de la constante mágica.
    """
    if cantidad_filas == cantidad_columnas:
        contante_magica = (cantidad_filas*((cantidad_filas**2) + 1)) / 2
    return contante_magica

def verificar_filas_magicas(matriz: list, contante_magica: int) -> bool:
    """Verifica si la sumatoria individual de cada fila, es igual a la constante mágica.

    Args:
        matriz (list): Matriz a evaluar sus filas.
        contante_magica (int): Constante a comparar con la sumatoria de cada fila.

    Returns:
        bool: True si todas las filas son mágicas (False caso contrario)
    """
    for i in range(len(matriz)):
        comparador = 0
        for j in range(len(matriz[i])):
            comparador += matriz[i][j]
        if comparador != contante_magica:
            fila_magica =  False
            break
        else:
            fila_magica = True
    return fila_magica

def verificar_columnas_magicas(matriz: list, contante_magica: int) -> bool:
    """Verifica si la sumatoria individual de cada columna, es igual a la constante mágica.

    Args:
        matriz (list): Matriz a evaluar sus columnas.
        contante_magica (int): Constante a comparar con la sumatoria de cada columna.

    Returns:
        bool: True si todas las columnas son mágicas (False caso contrario)
    """
    for i in range(len(matriz)):
        comparador = 0
        for j in range(len(matriz[i])):
            comparador += matriz[j][i]
        if comparador != contante_magica:
            columna_magica =  False
            break
        else:
            columna_magica = True        
    return columna_magica

def verificar_diagonal_principal_magica(matriz: list, contante_magica: int) -> bool:
    """Verifica si la sumatoria de la diagonal principal, es igual a la constante mágica.

    Args:
        matriz (list): Matriz a evaluar sus¿ diagonal principal.
        contante_magica (int): Constante a comparar con la sumatoria de la diagonal principal.

    Returns:
        bool: True si la diagonal principal es mágicas (False caso contrario)
    """
    comparador = 0
    for i in range(len(matriz)):
        comparador += matriz[i][i]
    if comparador != contante_magica:
        diagonal_principal_magica = False
    else:
        diagonal_principal_magica = True
    return diagonal_principal_magica

def verificar_diagonal_secundaria_magica(matriz: list, contante_magica: int) -> bool:
    """Verifica si la sumatoria de la diagonal secundaria, es igual a la constante mágica.

    Args:
        matriz (list): Matriz a evaluar sus diagonal secundaria.
        contante_magica (int): Constante a comparar con la sumatoria de la diagonal secundaria.

    Returns:
        bool: True si la diagonal secundaria es mágicas (False caso contrario)
    """
    comparador = 0
    for i in range(len(matriz)):
        comparador += matriz[i][len(matriz)-i-1]
    if comparador != contante_magica:
        diagonal_secundaria_magica = False
    else:
        diagonal_secundaria_magica = True
    return diagonal_secundaria_magica

def verificar_cubo_magico(matriz: list, constante: int) -> bool:
    """Funcion que comprueba las verificaciones de filas, columnas y diagonales, con la constante mágica.

    Args:
        matriz (list): Matriz a evaluar todas sus sumatorias.
        constante (int): Constante mágica.

    Returns:
        bool: True si la matriz se trata de un cuadrado mágico (False caso contrario).
    """
    es_magico = False
    check_1 = verificar_filas_magicas(matriz, constante)
    if check_1:
        check_2 = verificar_columnas_magicas(matriz, constante)
        if check_2:
            check_3 = verificar_diagonal_principal_magica(matriz, constante)
            if check_3:
                check_4 = verificar_diagonal_secundaria_magica(matriz, constante)
                if check_4:
                    es_magico = True
    return es_magico


import random
from validate import *

def solicitar_entero(mensaje: str, mensaje_error: str, min_val: int, max_val: int) -> int:
    """Funcion para solicitar un número entero al usuario, y validar si es un int, float o str, dentro de un rango máximo y mínimo

    Args:
        mensaje (str): Mensaje a mostrarle al usuario.
        mensaje_error (str): Mensaje de error a mostrarle al usuario.
        min_val (int): Límite inferior para los valores N° permitidos a ingresar.
        max_val (int): Límite superior para los valores N° permitidos a ingresar.

    Returns:
        int: Devuelve un N° entero
    """
    bandera_entero = False
    while bandera_entero == False:
        numero_entero = input(mensaje)
        validar = validar_numero(numero_entero, min_val, max_val)
        if validar:
            numero_entero = int(numero_entero)
            bandera_entero = True
        else:
            mensaje = mensaje_error
    return numero_entero

def cargar_matriz(matriz: list, mensaje: str, mensaje_error: str, rango: int, auto: bool = False,) -> list:
    """Funcion para cargar una matriz de N° de forma manual o automática, sin repetir los valores internos dentro del rango permitido.

    Args:
        matriz (list): Matriz a la cual cargar sus valores.
        mensaje (str): Mensaje para el usuario (Caso manual).
        mensaje_error (str): Mensaje de error para el usuario (Caso manual).
        rango (int): Rango de la matriz.
        auto (bool, optional): Booleano para la carga automática de la matriz (True). Defaults to False.

    Returns:
        list: Devuelve la matriz con todos los valores cargados.
    """
    lista_usados = []
    mensaje_guardado = mensaje
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            bandera_verificacion = True
            mensaje = mensaje_guardado
            while bandera_verificacion:
                if auto:
                    numero = random.randint(1, rango**2)
                else:
                    numero = solicitar_entero(mensaje + f"{i},{j} ", mensaje_error, 1, rango**2)

                numero_a_verificar = verificar_repetido_lista(lista_usados, numero)

                if numero_a_verificar == False:
                    matriz[i][j] = numero
                    lista_usados += [numero]
                    bandera_verificacion = False
                    
                else:
                    mensaje = mensaje_error                
    return matriz

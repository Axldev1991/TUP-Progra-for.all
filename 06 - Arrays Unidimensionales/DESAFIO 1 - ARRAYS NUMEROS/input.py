import random
from especificas import *

def ingresar_datos(mensaje: str, mensaje_error: str, auto: bool) -> list:
    """Solicita al usuario el ingreso de 10 N° y se cargan en una lista (Opcional: la carga se realiza de manera automática).

    Args:
        mensaje (str): Mensaje de solicitud al usuario.
        mensaje_error (str): Mensaje de error para el usuario.
        auto (bool): True -> Carga automática (Sin solicitud al usuario)

    Returns:
        list: _description_
    """
    list = [0] * 10
    for i in range(10):
        if auto:
            list[i] = solicitar_entero(mensaje, mensaje_error, -1000, 1000)
        else:
            list[i] = random.randint(-1000,1000)
    return list

def solicitar_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    """Solicita al usuario un N° entero.

    Args:
        mensaje (str): Mensaje de solicitus a mostrar en pantalla.
        mensaje_error (str): Mensaje de error en caso de que el ingreso no sea válido.
        minimo (int): Mínimo valor que pueda ingresar el usuario.
        maximo (int): Máximo valor que pueda ingresar el usuario.

    Returns:
        int: Devuelve el número ingresado por el usuario.
    """
    bandera_entero = False
    while bandera_entero == False:
        numero_entero = input(mensaje)
        validar = validar_numero(numero_entero, minimo, maximo)
        if validar:
            numero_entero = int(numero_entero)
            bandera_entero = True
        else:
            mensaje = mensaje_error
    return numero_entero
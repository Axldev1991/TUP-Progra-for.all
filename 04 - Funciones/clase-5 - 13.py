#13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

from colorama import Fore, Back, init
init()

def soliticar_entero (mensaje: str, mensaje_error: str) -> int:
    """Solicita y verifica el ingreso de un número entero.
    Args:
        mensaje (str): Mensaje a mostrar para el ingreso del dato.
        mensaje_error (str): Mensaje de error y de nueva solicitud del dato.
    Returns:
        int: Dato Entero.
    """
    entero = input(mensaje)
    while float(entero) % 1 != 0:
        entero = input(Fore.RED + mensaje_error + Fore.RESET)
    return int(entero)


def soliticar_flotante (mensaje: str, mensaje_error: str) -> float:
    """Solicita y verifica el ingreso de un número decimal.
    Args:
        mensaje (str): Mensaje a mostrar para el ingreso del dato.
        mensaje_error (str): Mensaje de error y de nueva solicitud del dato.
    Returns:
        float: Dato decimal.
    """
    flotante = input(mensaje)
    while float(flotante) % 1 == 0:
        flotante = input(Fore.RED + mensaje_error + Fore.RESET)
    return float(flotante)


def soliticar_cadena (mensaje: str) -> str:
    """Solicita el ingreso de un texto / oración.
    Args:
        mensaje (str): Mensaje a mostrar para el ingreso del texto.
    Returns:
        str: Texto ingresado.
    """
    cadena = input(Back.BLUE + Fore.WHITE + mensaje)
    return cadena


soliticar_entero("Ingrese un número entero: ", "Error. Asegurese de ingresar un número entero: ")
soliticar_flotante("Por favor, ingrese un numero decimal: ", "NO, ESO NO ES DECIMAL: ")
soliticar_cadena("Escriba una palabra o una frase breve: ")

# https://onlinegdb.com/5MjG6K-HA
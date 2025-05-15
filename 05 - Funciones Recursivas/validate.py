from utils import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    retorno_entero = None
    for i in range (reintentos + 1):
        numero_entero = input(mensaje)
        validar_entero = validate_number(numero_entero, minimo, maximo)        
        if validar_entero == True:
            retorno_entero = int(numero_entero)
            break
        else:
            mensaje = mensaje_error
    return retorno_entero
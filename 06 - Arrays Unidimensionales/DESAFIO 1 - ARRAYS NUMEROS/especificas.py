def verificar_positivo(numero: int) -> bool:
    """Verifica si un número entero es positivo.

    Args:
        numero (int): Recibe un N° entero.

    Returns:
        bool: Devuelve True en el caso de que el N° sea positivo (caso contrario, False).
    """
    if numero >= 0:
        verificador = True
    else:
        verificador = False
    return verificador

def verificar_par(numero: int) -> bool:
    """Verifica si un número entero es par.

    Args:
        numero (int): Recibe un N° entero.

    Returns:
        bool: Devuelve True en el caso de que el N° sea par (caso contrario, False).
    """
    if numero % 2 == 0 or numero == 0:
        verificador = True
    else:
        verificador = False
    return verificador

def validar_numero (numero, minimo, maximo) -> bool:
    """Valida si un dato recibido es un dato de tipo INT o FLOAT, y comprueba que esté en un rango de valores.

    Args:
        numero (_type_): Dato que recibe a verificar el tipo.
        minimo (_type_): Límite inferior en el que puede encontrarse el N°.
        maximo (_type_): Límite superior en el que puede encontrarse el N°.

    Returns:
        bool: Devuelve True para un N° ENTERO, False para un N° FLOAT, None para un STR
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


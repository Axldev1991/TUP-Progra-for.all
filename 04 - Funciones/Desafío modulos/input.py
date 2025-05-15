import validate

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    retorno_entero = None
    for i in range (reintentos + 1):
        numero_entero = input(mensaje)
        validar_entero = validate.validate_number(numero_entero, minimo, maximo)        
        if validar_entero == True:
            retorno_entero = int(numero_entero)
            break
        else:
            mensaje = mensaje_error

    return retorno_entero

###############################################

def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:
    retorno_flotante = None
    for i in range (reintentos + 1):
        numero_decimal = input(mensaje)
        validar_decimal = validate.validate_number(numero_decimal, minimo, maximo)

        if validar_decimal == False:
            retorno_flotante = float(numero_decimal)
        else:
            mensaje = mensaje_error
    
    return retorno_flotante

###############################################

def get_string(mensaje: str, mensaje_error: str, longitud_minima: int , longitud_maxima: int, reintentos: int) -> str|None:
    retorno_cadena = None
    for i in range(reintentos+1):
        texto = input(mensaje)
        validar_cadena = validate.validate_length(texto, longitud_minima, longitud_maxima)
        if validar_cadena == True:
            retorno_cadena = texto
        else:
            mensaje = mensaje_error
    return retorno_cadena

# get_string("numero: ", "error: ", 4, 10, 3)

# 1.0 https://onlinegdb.com/C04D88Ej2
# 2.0 https://onlinegdb.com/UQ7DjgrJo
def validate_number(numero, minimo, maximo):
    retorno_number = None
    if numero.isalpha() == False:
        numero = float(numero)
        if numero >= minimo and numero <= maximo:
            if numero % 1 == 0:
                retorno_number = True
            else:
                retorno_number = False
        return retorno_number

def validate_length(texto, longitud_minima, longitud_maxima):
    retorno_validate_length = None
    if len(texto) >= longitud_minima and len(texto) <= longitud_maxima:
        retorno_validate_length = True
    else:
        retorno_validate_length = False
    return retorno_validate_length
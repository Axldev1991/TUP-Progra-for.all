def validate_number(numero, minimo, maximo):
    if numero.isalpha() == False:
        numero = float(numero)
        if numero >= minimo and numero <= maximo:
            if numero % 1 == 0:
                return True
            return False
        
def validate_length(texto, longitud_minima, longitud_maxima):
    if len(texto) >= longitud_minima and len(texto) <= longitud_maxima:
        return True
    return False
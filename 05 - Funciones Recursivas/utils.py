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
        

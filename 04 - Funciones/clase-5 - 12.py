#12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def mostrar_tabla_multiplicar (numero: int, minimo: int = 1, maximo: int = 10) -> True|False:
    """Muestra la tabla de multiplicar de un número

    Args:
        numero (int): Número del cual se debe crear la tabla
        minimo (int, optional): Límite inferior del cuál se desea arrancar la tabla. Por default es 1.
        maximo (int, optional): Límite superior del cuál se desea finalizar la tabla. por default es 10

    Returns:
        True|False: True -> parámetros correctos. | False -> error con alguno/s de los parámetros
        
    """
    if type(minimo) == int and type(maximo) == int:
        for i in range(minimo, maximo + 1):
            multiplicacion = numero * i
            print(f"{numero} X {i} = {multiplicacion}")
        return True
    
    return False

primer_numero = 2.1
segundo_numero = 10
tercer_numero = 4

mostrar_tabla_multiplicar(primer_numero)

# mostrar_tabla_multiplicar(segundo_numero, 3)
# mostrar_tabla_multiplicar(tercer_numero, 2, 7)

# https://onlinegdb.com/DON4gItyy

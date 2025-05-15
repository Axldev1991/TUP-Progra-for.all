#3 Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
import sys
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

def sumar_digitos(numero: int) -> int:
    if numero < 10:
        resultado = numero
    else:
        ultimo_digito = numero % 10
        resto_del_numero = numero // 10
        resultado = ultimo_digito + sumar_digitos(resto_del_numero)
    return resultado

    # if numero > 0:
    #     unidad = len(str(numero))
    #     division = 10**(unidad-1)
    #     resta = int(numero/division) * division
    #     resultado = int(numero / division) + sumar_digitos(numero - resta)        
    # else:
    #     resultado = 0
    # return resultado

def main() -> None:    
    x = get_int("Ingrese un número entero: ", "Error... Ingrese un número entero: ", 0, 10000, 3)
    z = sumar_digitos(x)
    print(f"La suma de los dígitos es: {z}")

if __name__ == "__main__":
    sys.exit(main())

# https://onlinegdb.com/QZ-7Svs-R
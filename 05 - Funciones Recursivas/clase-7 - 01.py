#1 Realizar una función recursiva que calcule la suma de los primeros números naturales:
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

def sumar_naturales(numero: int) -> int:
    ### NO USAR DOBLE RETURN!!!!!!!!!!!!
    
    if numero == 0:
        resultado = 0         
    else:
        resultado = numero + sumar_naturales(numero - 1)
    
    return resultado

def main() -> None:
    x = get_int("Ingrese un número entero: ", "Error... Ingrese un número entero: ", 0, 100, 3)
    y = sumar_naturales(x)
    print(f"el resultado es: {y}")

if __name__ == "__main__":
    sys.exit(main())

# https://onlinegdb.com/iTUIoBYVj
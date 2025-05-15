#2 Realizar una función recursiva que calcule la potencia de un número:
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

def calcular_potencia(base: int, exponente:int ) -> int:
    if exponente > 0:
        resultado = base * calcular_potencia(base, exponente - 1)
    else:
        resultado = 1
    return resultado

def main() -> None:    
    x = get_int("Ingrese un número entero para la base: ", "Error... Ingrese un número entero: ", 0, 100, 3)
    y = get_int("Ingrese un número entero para el exponente: ", "Error... Ingrese un número entero: ", 0, 100, 3)
    z = calcular_potencia(x, y)
    print(f"El resultado es: {z}")

if __name__ == "__main__":
    sys.exit(main())

# https://onlinegdb.com/Mya5EfYkNJ
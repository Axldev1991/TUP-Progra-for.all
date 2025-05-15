#4 La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
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

def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        resultado = 0        
    elif numero == 1:
        resultado = 1
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci (numero - 2)
        #print(resultado)
    return resultado

def main() -> None:    
    x = get_int("Ingrese un número entero: ", "Error... Ingrese un número entero: ", 0, 30, 3)
    z = calcular_fibonacci(x)
    print(f"La sucesion de Fibonacci es: {z}")

if __name__ == "__main__":
    sys.exit(main())

# https://onlinegdb.com/Q87nRCBJi9
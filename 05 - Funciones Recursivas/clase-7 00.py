from validate import *

#1 Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero: int) -> int:
    ### NO USAR DOBLE RETURN!!!!!!!!!!!!
    
    if numero == 0:
        resultado = 0         
    else:
        resultado = numero + sumar_naturales(numero - 1)
    
    return resultado



#2 Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base: int, exponente:int ) -> int:
    if exponente > 0:
        resultado = base * calcular_potencia(base, exponente - 1)
    else:
        resultado = 1
    return resultado  
    


#3 Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

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

x = sumar_digitos(1234)
print(x)

#4 La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:

def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        resultado = 0        
    elif numero == 1:
        resultado = 1
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci (numero - 2)
        #print(resultado)
    return resultado

# x = calcular_fibonacci(get_int("Escriba un número entero: ", "Error, escriba un número entero: ", 0, 40, 3))
# print(f"El número de Fibonacci es: {x}")
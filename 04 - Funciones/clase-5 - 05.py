#5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

import math

def calcular_area_circulo(radio: int|float) -> float|None:
    """Calcula el área de un círculo.
    Args:
        radio (int | float): Radio del círculo a calcular el área.
    Returns:
        float: Área del círculo.
        \n None: Hubo un error al ingresar el radio
    """
    area = None
    if (type(radio) == int or type(radio) == float):
        area = radio**2 * math.pi #
    return area

radio = int(input("Ingrese el radio: "))#10
area_calculada = calcular_area_circulo(radio)
print(f"El area del círculo es: {area_calculada}")

# https://onlinegdb.com/15quVB-8IY
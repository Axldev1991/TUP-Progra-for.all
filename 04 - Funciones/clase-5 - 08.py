#8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo(numero_uno, numero_dos, numero_tres):
    maximo = numero_uno
    if numero_dos > maximo:
        maximo = numero_dos
    if numero_tres > maximo:
        maximo = numero_tres
    return maximo

numero_uno = -100
numero_dos = -15
numero_tres = -500

maximo_numero = encontrar_maximo(numero_uno, numero_dos, numero_tres)
print(f"{maximo_numero}")

# https://onlinegdb.com/qBVMoVuxL
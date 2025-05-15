#9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potenciar_numero(base, exponente):
    resultado_potencia = base ** exponente
    return resultado_potencia

base = 5
exponente = 3

potencia = potenciar_numero(base, exponente)
print(f"{potencia}")

# https://onlinegdb.com/NfYxB8KE_
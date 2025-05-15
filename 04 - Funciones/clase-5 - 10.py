#10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def encontrar_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

numero = 13.2
funcion_primo = encontrar_primo(numero)
print(f"{funcion_primo}")

# https://onlinegdb.com/cJ36JWv0T
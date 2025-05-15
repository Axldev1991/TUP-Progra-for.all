#7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 12
paridad = verificar_par(numero)
print(f"El número {numero} es par??? {paridad}")

# https://onlinegdb.com/9uMRgtBaF
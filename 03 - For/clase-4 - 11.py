#11 Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un número: "))
contador = 0

for i in range(2, numero+1):    
    bandera_divisor = False
    
    for j in range(2, i):
        if i % j == 0:
            bandera_divisor = True
            break

    if bandera_divisor == True:        
        continue

    else:
        contador += 1
        print(f"BRAVO! {i} ES primo {contador}")

# https://onlinegdb.com/o1Ma2Jk9Bg
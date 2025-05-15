#10 Ingresar un número. Determinar si el número es primo o no.

# SE PUEDE OPTIMIZAR CON UNA BANDERA PARA NO RECORRER TODO EL BUCLE

numero = int(input("Ingrese un número: "))
contador = 0

for i in range(2, numero):
    
    if numero % i == 0:        
        contador += 1

if contador > 0:
    print(f"El número {numero} NO es primo")

else:
    print(f"BRAVO! {numero} ES primo")

# https://onlinegdb.com/rUUjkrPib
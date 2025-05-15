#2 Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos

i = 0
# clave = asd123

while i < 3:

    clave = input("Ingrese su clave: ")

    if clave == "asd123":
        print("La clave es correcta!")
        break

    print("Error. Clave incorrecta")
    
    i += 1

if i == 3:
    print("Contacte con su entidad para reiniciar la clave")

# https://onlinegdb.com/KPO-vNjgA
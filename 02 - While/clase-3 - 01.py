#1 Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = input("Ingrese su clave: ")

# clave = asd123
while clave != "asd123":

    clave = input("Error. Ingrese su clave: ")

print("la clave es correcta!")

# https://onlinegdb.com/slog44w9l
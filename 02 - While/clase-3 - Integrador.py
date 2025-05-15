#Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
    # Los datos requeridos son:
        # Apellido
        # Edad, entre 18 y 90 años inclusive.
        # Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
        # Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

        # Una vez ingresados y validados los datos, mostrarlos por pantalla.

edad = 0

while edad < 18 or edad > 90:
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    if edad < 18 or edad > 90:
            print(f"La persona de apellido {apellido} es menor de edad o supera los 90 años. Ingrese a otra persona")

estado_civil = input("Indique su estado civil (Soltero/Casado/Divorciado/Viudo): ")
legajo = int(input("Ingrese su número de legajo: "))

# while len(str(legajo)) != 4:
#     legajo = int(input("Error. Recuerde que el legajo contiene 4 dígitos y que el primero no puede ser 0. \n Ingrese nuevamente su legajo: "))

######### PROFE GONZA: NO SÉ SI ESTA ES LA MANERA CORRECTA, YA QUE NO VALIDO SI EL PRIMER DÍGITO ES 0, PERO FUNCIONA DE IGUAL MANERA. 
######### PROFE GONZA: NO SÉ SI ESTA ES LA MANERA CORRECTA, YA QUE NO VALIDO SI EL PRIMER DÍGITO ES 0, PERO FUNCIONA DE IGUAL MANERA. 
######### PROFE GONZA: NO SÉ SI ESTA ES LA MANERA CORRECTA, YA QUE NO VALIDO SI EL PRIMER DÍGITO ES 0, PERO FUNCIONA DE IGUAL MANERA. 
######### PROFE GONZA: NO SÉ SI ESTA ES LA MANERA CORRECTA, YA QUE NO VALIDO SI EL PRIMER DÍGITO ES 0, PERO FUNCIONA DE IGUAL MANERA. 
######### PROFE GONZA: NO SÉ SI ESTA ES LA MANERA CORRECTA, YA QUE NO VALIDO SI EL PRIMER DÍGITO ES 0, PERO FUNCIONA DE IGUAL MANERA. 

while legajo < 1000 or legajo > 9999:
    legajo = int(input("Error. Recuerde que el legajo contiene 4 dígitos y que el primer dígito no puede ser 0. \n Ingrese nuevamente su legajo: "))
    

print("\n CARGA FINALIZADA")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"N° de legajo: {legajo}")

# https://onlinegdb.com/u0NhkaZX-
# https://onlinegdb.com/lAbJu7ReB
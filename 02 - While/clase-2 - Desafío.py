# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)

# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

# CORRECIONES CORRECIONES CORRECIONES CORRECIONES CORRECIONES CORRECIONES CORRECIONES CORRECIONES
# No valida genero ni tecnologia. La validacion de edad no esta bien, va a pedir el nombre siempre que la edad este mal. No es necesario inicializar edad. Para el punto 2 de analisis de datos no tenes en cuenta la opcion de genero "Otro". 


i = 0
cantidad_masculinos_ia_iot = 0
voto_no_ia = 0
edad_mayor_masculino = 0
nombre_mayor_masculino = 0
tecnologia_mayor_masculino = 0

while i < 5:        

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    
    while edad < 18:
        edad = int(input("Ingrese su edad: "))

        if edad < 18:
            print(f"El empleado {nombre} es menor de edad. Ingrese otro empleado")

    genero = input("Ingrese su género: (Masculino/Femenino/Otro): ")
    tecnologia = input("Ingrese la tecnología: (IA - RV/RA - IOT): ")

    if genero == "Masculino":
            if tecnologia != "RV/RA" and edad >= 25 and edad <= 50:
                cantidad_masculinos_ia_iot += 1

            if tecnologia != "IA" and edad >= 33 and edad <= 40:
                voto_no_ia += 1

            if edad > edad_mayor_masculino:
                edad_mayor_masculino = edad
                nombre_mayor_masculino = nombre
                tecnologia_mayor_masculino = tecnologia
    i += 1

porcentaje_no_ia = 0

if voto_no_ia > 0 or cantidad_masculinos_ia_iot > 0:
    porcentaje_no_ia = voto_no_ia / i * 100

    print(f"La cantidad de empleados MASCULINOS que eligieron IOT o IA: {cantidad_masculinos_ia_iot}")
    print(f"El porcentaje de empleados que NO votaron IA: %{porcentaje_no_ia}")
    print(f"El empleado MASCULINI de mayor edad se llama {nombre_mayor_masculino} y tiene {edad_mayor_masculino} años")

else:
    print("Carga completa. Fin")

# https://onlinegdb.com/4FaINCr6hx

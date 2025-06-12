# Verificación de Cadena Alfabética
# Objetivo: Crear una función que determine si una cadena está compuesta únicamente por letras mayúsculas y minúsculas (sin espacios, números ni símbolos).
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Comparar los caracteres con los valores ASCII para determinar si son letras.
#   No se pueden usar métodos como .isalpha().

def verificar_mayus_minus(cadena: str) -> bool:
    cadena_valida = True
    for i in range(len(cadena)):
        if ord(cadena[i]) < 65 or (ord(cadena[i]) > 90 and ord(cadena[i]) < 97) or ord(cadena[i]) > 122:
            cadena_valida = False
            break
    return cadena_valida

# Validación de Número Entero
# Objetivo: Implementar una función que verifique si una cadena representa un número entero válido (positivo o negativo). 
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Validar que el primer carácter puede ser un signo + o - (opcional).
#   Los demás caracteres deben ser únicamente dígitos (0-9).
#   No se pueden usar .isdigit().

def validar_entero(cadena: str) -> bool:
    entero_valido = True
    if len(cadena) == 0 or cadena == "+" or cadena == "-":
        entero_valido = False
    else:
        for i in range(len(cadena)):
            if cadena[i] < "0" or cadena[i] > "9":
                if i == 0 and (cadena[i] == "-" or cadena[i] == "+"):
                    continue
                else:
                    entero_valido = False
                    break
    return entero_valido

# Validación de Número Decimal
# Objetivo: Escribir una función que determine si una cadena representa un número decimal válido con un solo punto decimal.
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Validar que el primer carácter puede ser un signo + o - (opcional).
#   Solo se permite un punto decimal dentro de la cadena.
#   Todos los demás caracteres deben ser dígitos (0-9).
#   No se pueden usar .isdigit() ni .isdecimal().

def validar_decimal(cadena: str) -> bool:
    cadena_decimales = ".0123456789"
    decimal_valido = True
    if len(cadena) == 0 or cadena == "+" or cadena == "-" or cadena == ".":
        decimal_valido = False
    else:
        inicio = 0
        if cadena[0] == "+" or cadena[0] == "-":
            inicio = 1

        contador_puntos = 0
        for i in range(inicio, len(cadena)):
            caracter_valido = False
            for j in range(len(cadena_decimales)):
                if cadena[i] == cadena_decimales[j]:
                    caracter_valido = True
                    break
            if caracter_valido:
                if cadena[i] == ".":
                    contador_puntos += 1
                if contador_puntos > 1:
                    decimal_valido = False
                    break
            else:
                decimal_valido = False
                break
    return decimal_valido

# Validación de Clave Segura
# Objetivo: Crear una función que valide si una contraseña cumple con las siguientes condiciones:
# Contiene al menos una letra mayúscula.
# Contiene al menos una letra minúscula.
# Contiene al menos un número.
# Tiene al menos 8 caracteres de longitud.
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Determinar el tipo de cada carácter comparándolo con su valor ASCII.
#   No se pueden usar .isupper(), .islower(), .isdigit(), etc.

def validar_clave(cadena: str) -> bool:
    contador_mayus = 0
    contador_minus = 0
    contador_num = 0
    clave_valida = True
    if len(cadena) < 8:
        clave_valida = False
    else:
        for i in range(len(cadena)):
            if ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90:
                contador_mayus += 1
            if ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122:
                contador_minus += 1
            if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                contador_num += 1
        if contador_mayus < 1 or contador_minus < 1 or contador_num < 1:
            clave_valida = False
    return clave_valida


# Verificación de Palíndromo
# Objetivo: Crear una función que determine si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda, sin distinguir mayúsculas y minúsculas).
# Restricciones:
#   Recorrer la cadena sin usar métodos como [::-1].
#   Convertir letras mayúsculas a minúsculas manualmente.
#   Comparar caracteres desde ambos extremos de la cadena.

def verificar_palindromo(cadena: str) -> bool:
    nueva_cadena = ""
    cadena_volteada = ""
    palindromo_valido = False
    for i in range(len(cadena)):
        caracter = cadena[i]
        if ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90:
            caracter = chr(ord(cadena[i]) + 32)
        if ord(cadena[i]) == 32:
            continue
        nueva_cadena += caracter
    
    longitud = len(nueva_cadena)
    for j in range(longitud -1, -1, -1):
        caracter = nueva_cadena[j]
        cadena_volteada += caracter

    if nueva_cadena == cadena_volteada:
        palindromo_valido = True

    return palindromo_valido

# Validación de Correo Electrónico
# Objetivo: Escribir una función que valide si una cadena tiene el formato de un correo electrónico válido, cumpliendo las siguientes reglas:
# Debe contener exactamente un "@".
# Debe haber al menos un carácter antes y después del "@".
# Debe contener un punto "." después del "@", con al menos dos caracteres después del punto.
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Contar la cantidad de "@" y ".".
#   No se pueden usar expresiones regulares ni .count().

def validar_email(cadena: str) -> bool:
    contador_arroba = 0
    contador_punto = 0
    direccion = ""
    dominio = ""
    tld = ""
    existe_arroba = False
    existe_punto = False
    email_valido = True
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter == "@":
            contador_arroba += 1
            existe_arroba = True
        if caracter == ".":
            contador_punto += 1
            existe_punto = True
        if existe_arroba and existe_punto == False:
            dominio += caracter
        elif existe_punto:
            tld += caracter
        else:
            direccion += caracter
    if contador_arroba > 1 or contador_punto > 1 or len(direccion) < 1 or len(dominio) < 3 or len(tld) < 3:
        email_valido = False
    
    return email_valido

# Contador de Vocales y Consonantes
# Objetivo: Implementar una función que reciba una cadena y cuente la cantidad de vocales y consonantes.
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Comparar manualmente con los valores ASCII o con listas de vocales (a, e, i, o, u).
#   No se pueden usar .isalpha().

def contar_vocales_consonantes(cadena: str) -> list:
    vocales = "AEIOUaeiou"
    vocales_consonantes = [0,0]
    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122:
            es_vocal = False
            for j in range(len(vocales)):
                if cadena[i] == vocales[j]:
                    es_vocal = True
                    break
            if es_vocal:
                vocales_consonantes[0] += 1
            else:
                vocales_consonantes[1] += 1
    
    return vocales_consonantes

# Validación de Número de Teléfono
# Objetivo: Crear una función que determine si una cadena representa un número de teléfono válido. Un número de teléfono válido debe cumplir las siguientes condiciones:
# Debe tener exactamente 10 dígitos numéricos.
# El número debe empezar con un dígito válido según el país (por ejemplo, en muchos países empieza con un 9 o 2).
# No debe contener caracteres especiales, como guiones o espacios.
# No puede empezar con un cero a menos que sea un número de teléfono específico (ejemplo: para algunos países, el número de teléfono empieza con 9).
# Restricciones:
#   Recorrer la cadena carácter por carácter.
#   Verificar que todos los caracteres sean dígitos (0-9).
#   Asegurarse de que la cadena tenga exactamente 10 caracteres.
#   No usar métodos como .isdigit() ni .len().
#   Asegurarse de que el número no empiece con un cero (excepto en casos específicos si se permite).

def validar_telefono(cadena: str) -> bool:
    telefono_valido = True

    while True:
        if len(cadena) != 10:
            telefono_valido = False
            break

        if cadena[0] != "9" and cadena[0] != "2":
            telefono_valido = False
            break

        else:
            for i in range(10):
                if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
                    telefono_valido = False
                    break
            break
    return telefono_valido


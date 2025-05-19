import random

def validar_numero (numero, minimo: int, maximo: int) -> int:
    bandera_validacion = None
    if numero.isalpha() == False:
        numero = float(numero)
        if numero >= minimo and numero <= maximo:
            if numero % 1 == 0:
                bandera_validacion = True
            else:
                bandera_validacion = False
        return bandera_validacion


def solicitar_entero(mensaje: str, mensaje_error: str, min_val: int, max_val: int) -> int:
    bandera_entero = False
    while bandera_entero == False:
        numero_entero = input(mensaje)
        validar = validar_numero(numero_entero, min_val, max_val)
        if validar:
            numero_entero = int(numero_entero)
            bandera_entero = True
        else:
            mensaje = mensaje_error
    return numero_entero


def crear_matriz(filas: int, columnas: int, contenido: int = 0) ->list:
    matriz = [[contenido] * columnas for _ in range(filas)]    
    return matriz

def verificar_repetido_lista(lista: list, numero: int) -> bool:
    bandera = False
    for i in range(len(lista)):
        if numero == lista[i]:
            bandera = True
            break
    return bandera

def cargar_matriz(matriz: list, mensaje: str, mensaje_error: str, rango: int, auto: bool = False,) -> list:
    lista_usados = []
    mensaje_guardado = mensaje
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            bandera_verificacion = True
            mensaje = mensaje_guardado
            while bandera_verificacion:
                if auto:
                    numero = random.randint(1, rango**2)
                else:
                    numero = solicitar_entero(mensaje + f"{i},{j} ", mensaje_error, 1, rango**2)

                numero_a_verificar = verificar_repetido_lista(lista_usados, numero)

                if numero_a_verificar == False:
                    matriz[i][j] = numero
                    lista_usados += [numero]
                    bandera_verificacion = False
                    
                else:
                    mensaje = mensaje_error                
    return matriz

def mostrar_formato_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:>3}", end=" ")
        print("")

def calcular_contante_magica(cantidad_filas: int, cantidad_columnas: int) -> int:
    if cantidad_filas == cantidad_columnas:
        contante_magica = (cantidad_filas*((cantidad_filas**2) + 1)) / 2
    return contante_magica



##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
##################################### ELIMINAR EL WHILE YA QUE ES LO MISMO QUE EL FOR, Y UTILIZAR BREAK PARA ROMPER EL CICLO
def verificar_filas_magicas(matriz: list, cantidad_filas: int, contante_magica: int) -> bool:
    fila_a_recorrer = 0
    while fila_a_recorrer < cantidad_filas:
        comparador = 0
        for i in range(cantidad_filas):
            comparador += matriz[fila_a_recorrer][i]
        if comparador != contante_magica:
            fila_magica =  False
        else:
            fila_magica = True
        fila_a_recorrer += 1
    return fila_magica

def verificar_columnas_magicas(matriz: list, cantidad_columnas: int, contante_magica: int) -> bool:
    columna_a_recorrer = 0
    while columna_a_recorrer < cantidad_columnas:
        comparador = 0
        for i in range(cantidad_columnas):
            comparador += matriz[i][columna_a_recorrer]
        if comparador != contante_magica:
            columna_magica =  False
        else:
            columna_magica = True
        columna_a_recorrer += 1
    return columna_magica

def verificar_diagonal_principal_magica(matriz: list, cantidad_columnas: int, contante_magica: int) -> bool:
    comparador = 0
    for i in range(cantidad_columnas):
        comparador += matriz[i][i]
    if comparador != contante_magica:
        diagonal_principal_magica = False
    else:
        diagonal_principal_magica = True
    return diagonal_principal_magica

def verificar_diagonal_secundaria_magica(matriz: list, cantidad_columnas: int, contante_magica: int) -> bool:
    comparador = 0
    for i in range(cantidad_columnas):
        comparador += matriz[i][cantidad_columnas-i-1]
    if comparador != contante_magica:
        diagonal_secundaria_magica = False
    else:
        diagonal_secundaria_magica = True
    return diagonal_secundaria_magica

def verificar_cubo_magico(matriz: list, constante: int) -> bool:
    check_1 = verificar_filas_magicas(matriz, len(matriz), constante)
    check_2 = verificar_columnas_magicas(matriz, len(matriz), constante)
    check_3 = verificar_diagonal_principal_magica(matriz, len(matriz), constante)
    check_4 = verificar_diagonal_secundaria_magica(matriz, len(matriz), constante)

    if check_1 and check_2 and check_3 and check_4:
        es_magico = True
    else:
        es_magico = False
    return es_magico



x = crear_matriz(3, 3, -2)
cargar_matriz(x, "ingrese el valor en la posicion ", "error... ", len(x), False)
mostrar_formato_matriz(x)
w = calcular_contante_magica(len(x), len(x))
print(w)
q = verificar_cubo_magico(x, w)
print(q)


#primer funcion validadora de cubo magico
#def verificar_cubo_magico(matriz: list, constante: int) -> bool:
    #### RECORREMOS FILAS
    # recorrido = 0
    # n = len(matriz)
    # while recorrido < n:
    #     comparador = 0
    #     for i in range(n):
    #         comparador += matriz[recorrido][i]
    #     if comparador != constante:
    #         return False
    #     recorrido += 1

    #### RECORREMOS COLUMNAS
    # recorrido = 0
    # while recorrido < n:
    #     comparador = 0
    #     for i in range(n):
    #         comparador += matriz[i][recorrido]
    #     if comparador != constante:
    #         return False
    #     recorrido += 1

    #### RECORREMOS DIAGONALES
    # comparador = 0
    # for i in range(n):
    #     comparador += matriz[i][i]
    # if comparador != constante:
    #     return False

    # comparador = 0
    # for i in range(n):
    #     comparador += matriz[i][n-i-1]
    # if comparador != constante:
    #     return False
    # return True


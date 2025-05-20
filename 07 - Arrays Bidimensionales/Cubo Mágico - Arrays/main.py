import sys
import random
from os import system

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

def verificar_filas_magicas(matriz: list, contante_magica: int) -> bool:    
    for i in range(len(matriz)):
        comparador = 0
        for j in range(len(matriz[i])):
            comparador += matriz[i][j]
        if comparador != contante_magica:
            fila_magica =  False
            break
        else:
            fila_magica = True
    return fila_magica

def verificar_columnas_magicas(matriz: list, contante_magica: int) -> bool:
    for i in range(len(matriz)):
        comparador = 0
        for j in range(len(matriz[i])):
            comparador += matriz[j][i]
        if comparador != contante_magica:
            columna_magica =  False
            break
        else:
            columna_magica = True        
    return columna_magica

def verificar_diagonal_principal_magica(matriz: list, contante_magica: int) -> bool:
    comparador = 0
    for i in range(len(matriz)):
        comparador += matriz[i][i]
    if comparador != contante_magica:
        diagonal_principal_magica = False
    else:
        diagonal_principal_magica = True
    return diagonal_principal_magica

def verificar_diagonal_secundaria_magica(matriz: list, contante_magica: int) -> bool:
    comparador = 0
    for i in range(len(matriz)):
        comparador += matriz[i][len(matriz)-i-1]
    if comparador != contante_magica:
        diagonal_secundaria_magica = False
    else:
        diagonal_secundaria_magica = True
    return diagonal_secundaria_magica

def verificar_cubo_magico(matriz: list, constante: int) -> bool:
    es_magico = False
    check_1 = verificar_filas_magicas(matriz, constante)
    if check_1:
        check_2 = verificar_columnas_magicas(matriz, constante)
        if check_2:
            check_3 = verificar_diagonal_principal_magica(matriz, constante)
            if check_3:
                check_4 = verificar_diagonal_secundaria_magica(matriz, constante)
                if check_4:
                    es_magico = True        
    return es_magico

def crear_cubo_magico(matriz: list, constante: int) -> list:
    bandera_magica = False
    while bandera_magica == False:
        repetidos = True
        while repetidos:
            lista_usados = []        
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    bandera_verificacion = True                
                    while bandera_verificacion:
                        numero = random.randint(1, (len(matriz))**2)
                        numero_a_verificar = verificar_repetido_lista(lista_usados, numero)

                        if numero_a_verificar == False:
                            matriz[i][j] = numero
                            lista_usados += [numero]
                            bandera_verificacion = False
                        else:
                            continue
                checkfila = verificar_filas_magicas([matriz[i]], constante)
                if checkfila == False:
                    break
            if checkfila:
                repetidos = False
        check = verificar_cubo_magico(matriz, constante)
        if check:
            bandera_magica = True
    return matriz

def main():
    print("Bienvenido usuario! Siéntese cómodo y dígame usted, que desea hacer?")
    opcion = solicitar_entero("Opcion (1): Cargar matriz manualmente.\nOpción (2): cargar matriz automáticamente.\nOpción (3): Generar cuadrado mágico.\n", "Error, lea bien las opciones!!: ", 1, 3)

    rango = solicitar_entero("Que Rango debería tener la matriz?: ", "Error, el rango debe ser mayor a 3", 3, 5)

    constante_magica = calcular_contante_magica(rango, rango)

    match opcion:
        case 1:
            matriz = crear_matriz(rango, rango)
            cargar_matriz(matriz, f"Ingrese el valor en la posicion : ", f"Error, el N° ya fué ingresado o está fuera del rango (1 - {rango**2}): ", rango, False )
            print("\nUsted ingresó la siguiente matriz: ")
            mostrar_formato_matriz(matriz)
            print("Verifiquemos su poder mágico...")
            verificador = verificar_cubo_magico(matriz, constante_magica)
            system("pause")
            system("cls")
            if verificador:
                print("BRAVO! SU CUADRADO ES MÁGICO")
            else:
                print("Lamento decirle... su cuadrado no es más que eso...")
            mostrar_formato_matriz(matriz)
        case 2:
            matriz = crear_matriz(rango, rango)
            cargar_matriz(matriz, "", "", rango, True)
            print("\nHemos creado para usted la siguiente matriz: ")
            mostrar_formato_matriz(matriz)
            print("Verifiquemos su poder mágico...")
            verificador = verificar_cubo_magico(matriz, constante_magica)
            system("pause")
            system("cls")
            if verificador:
                print("BRAVO! SU CUADRADO ES MÁGICO")
            else:
                print("Lamento decirle... su cuadrado no es más que eso...")
            mostrar_formato_matriz(matriz)
        case 3:
            matriz_magica = crear_matriz(rango, rango, 0)
            matriz_magica = crear_cubo_magico(matriz_magica, constante_magica)
            print("ABRAKADABRA!")
            system("pause")
            system("cls")
            print("Este es un cuadrado mágico")
            mostrar_formato_matriz(matriz_magica)




if __name__ == "__main__":
    sys.exit(main())

# x = crear_cubo_magico()
# mostrar_formato_matriz(x)
# print(x)

############
# x = crear_matriz(3, 3, -2)
# cargar_matriz(x, "ingrese el valor en la posicion ", "error... ", len(x), False)
# mostrar_formato_matriz(x)
# w = calcular_contante_magica(len(x), len(x))
# print(w)
# q = verificar_cubo_magico(x, w)
# print(q)


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


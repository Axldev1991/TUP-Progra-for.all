# Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad. Por ejemplo, si la cadena ingresada es “murcielaguito”, la salida por pantalla deberá ser: (“a”: 1; “e”: 1; “i”: 2; “o”: 1; “u”:2)

vocales_encontradas = [
    ["a", "e", "i", "o", "u"],
    [0 for _ in range(5)]
]

def buscar_cantidad_vocales(cadena: str, matriz: list) -> list:
    for i in range(len(matriz[0])):
        for j in range(len(cadena)):
            if matriz[0][i] == cadena [j]:
                matriz[1][i] += 1
    return matriz

def mostrar_formato_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end =" ")
        print("")

x = buscar_cantidad_vocales("murcielaguito", vocales_encontradas)
mostrar_formato_matriz(x)
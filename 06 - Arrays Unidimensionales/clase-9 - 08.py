""" #8 Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
        a- Una lista de nombres (lista_nombres).
        b- Un nombre a buscar en la lista (nombre_antiguo).
        c- Un nombre de reemplazo (nombre_nuevo). """

lista = ["axel", "pedro", "francisco", "julian", "german", "gonzalo", "nahuel", "pedro", "pedro"]

def reemplazar_nombres(vector, nombre_antiguo, nombre_nuevo):
    contador_nombres_reemplazados = 0
    for i in range(len(vector)):
        if nombre_antiguo == vector[i]:
            vector[i] = nombre_nuevo
            contador_nombres_reemplazados += 1
    return contador_nombres_reemplazados
    

x = reemplazar_nombres(lista, "pedro", "nicolás")
print(x)



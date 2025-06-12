########### LISTAS 

#metodos para agregar elementos:

# lista = [1,5,7]

# lista.append(4)
# print(lista)

# lista.insert(2,99)

# for i in range(len(lista)):
#     print(lista[i])

#metodo para agregar una lista dentro de otra
# otra = [3,6,7]
# lista.extend(otra)

# for numero in lista:
#     print(numero)

#metodos para quitar elementos de una lista

# lista = [1,5,7,8,4,5,6]
            #REMOVE
# lista.remove(5)
# print(lista)
# lista.remove(500) #ValueError: list.remove(x): x not in list
# print(lista)

            #POP
# valor = lista.pop(3) #con este método puedo guardar el valor que "popeo"
# valor1 = lista.pop(-3) #funciona, toma el índice como si fueran todos negativos
# print(valor1)
# for i in lista:
#     print(i)

            #INDEX
# lista = [1,5,7,8,4,5,6]

# for numero in lista:
#     if numero == 5:
#         indice = lista.index(numero) #RETORNA SIEMPRE EL PRIMER INDICE
#         print(indice)

#metodo para voltear la lista

            #REVERSE

# lista = [1,5,7,8,4,5,6]

# lista.reverse()

# for numero in lista:
#     print(numero)

#metodo para ordenar la lista

            #SORT
# lista = [1,5,7,8,4,5,6]

# lista.sort() #ascendente
# lista.sort(reverse = True) #descendente
# print(lista)


# otra = lista
# otra.sort() #ordena ambas listas: "otra" y "lista" ya que "otra" apunta a "lista".

# print(otra)
# print(lista)
import copy

# copia = copy.copy(lista) #shallow copy, es "superficial"
# print(copia)

# copia.sort()
# print(copia)
# print(lista)

# lista = [[1,3],[4,6],[7,9]]
# copia = copy.copy(lista)

# # copia[0] = [100,100] #estoy funciona, porque la copia es superficial

# # print(copia)
# # print(lista)


# # copia[0][1] = 100 #esto modifica la lista original, ya que la copia es solo superficial
# copia = copy.deepcopy(lista)
# copia[0][1] = 100

# print(copia)
# print(lista)

# print(lista)

#metodo para limpiar la lista

            #CLEAR

# lista = [1,5,7,8,4,5,6]

# lista.clear() #vacía toda la lista
# print(lista)

# del lista
# print(lista) #elimina o destruye la lista


# TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS TUPLAS

# tupla = (5,9) #INMUTABLES!
# tupla[0] = 2 #TypeError: 'tuple' object does not support item assignment, inmutables!
# lista = [1,5,7,9]
# tupla = tuple(lista) #puedo convertir un elemento a tupla

# print(tupla[0]) #son indexables

# for elemento in tupla: #se pueden recorrer
#     print(elemento)

# tupla = (255,42,252)
# print(type(tupla))

# PATALLA = (500, 750)
# ROJO = (255, 45, 42)
# FUCSIA = (252, 42, 255)
# PUNTO = (50, 95)

# lista = list(FUCSIA)

# print(lista) #convierto la tupla en lista

# r, g, b = ROJO #desempaquetado, me sirve para cuando tengo pocos valores

# print(r)
# print(g)
# print(b)
# print(len(FUCSIA))

#metodo
# tupla = (5,6,5,5,6,9)
# print(tupla.count(5)) #cuenta cuantas veces se repite un valor dentro de la tupla/lista
# print(tupla.index(6))

# SETS SETS SETS SETS SETS SETS SETS SETS SETS SETS

#crear un set
# lista = [3,6,2]
# mi_set = {4,8,3,0,4,8,4,6,2,4,9,4,3,1,4,6,7,8} # SI SON MUTABLES, NO tienen indice pero son iterables
# mi_set = set{lista}

# for elemento in mi_set:
#     print(elemento)

# print(mi_set) #no imprime los repetidos, y los ordena, por lo tanto no respetan el orden

# mi_set = {5,9,2}
# mi_set.add(99) #agrega un elemento
# mi_set.add(199)

# for elemento in mi_set: #los agrega al set y los imprime, pero en un orden que vaya a saber uno cual es...
#     print(elemento)

# mi_set = {5,9,2}

# mi_set.remove(9) #elimino un elemento
# mi_set.discard(9) #también lo elimina
# mi_set.discard(90) #no hace nada si el elemento no existe en el set, pero no tira error
# mi_set.pop() #elimina el primer elemento

# for elemento in mi_set:
#     print(elemento)

# set_1 = {5,4,9,3}
# set_2 = {2,5,4,1}

# inter = set_1.intersection(set_2) #busca la intersección
# print(inter)

# union = set_1.union(set_2) #busca la union de los dos sets
# print(union)

# diferencia = set_1.difference(set_2) #busca la diferencia entre los dos sets
# print(diferencia)


# DICCIONARIOS DICCIONARIOS DICCIONARIOS DICCIONARIOS DICCIONARIOS DICCIONARIOS DICCIONARIOS

# nombre = "juan"
# edad = 25
# profesion = "Ingeniero"
# mail = "juancito@juan.com"

persona = {
    "nombre": ["juan", "pablo"],
    "edad": 25,
    "altura": 1.75,
    "esta_soltero": True
}

# print(type(persona))
# print(persona.keys())
# print(persona.values())
# print(persona.items())
# print(type(persona.items())) #CHEQUEAR!

# for clave in persona.keys():
#     print(f"Clave: {clave} -> Valor: {persona[clave]}")
#LO DE ARRIBA ES LO MISMO QUE ESTO:
# for clave in persona:
#     print(f"Clave: {clave} -> Valor: {persona[clave]}")
#OTRA FORMA DE HACERLO
# for clave, valor in persona.items():
#     print(f"Clave: {clave} -> Valor: {valor}")
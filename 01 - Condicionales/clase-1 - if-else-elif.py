altura = float(input("Ingrese la altura del jugador en cm: "))

if altura < 160:
    print("El jugador tendrá posición de: Base")

elif altura < 180:
    print("El jugador tendrá posición de: Escolta")

elif altura < 200:
    print("El jugador tendrá posición de: Alero")

else:
    print("El jugador tendrá posición de: Ala-Pívot o Pívot")

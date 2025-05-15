estacion = input("Ingrese en cual estación del año desea viajar: ")
destino = input ("Ingrese el destino ((1)Bariloche - (2)Mar del Plata - (3)Cataratas): ")


match estacion:
    case "invierno":
        if destino == "1":
            print("Se viaja")
        else:
            print("No se viaja")

    case "verano":
        if destino == "2" or destino == "3":
            print("Se viaja")
        else:
            print("No se viaja")

    case "otoño":
        print("Se viaja")

    case "primavera":
        if destino == "1":
            print("No se viaja")
        else:
            print("Se viaja")    
       


cliente = input("Ingrese su tipo de cliente ((R)Residencial - (C)Comercial - (I)Industrial): ")
consumo = float(input("Ingrese su consumo en m3 de agua: "))

TARIFA_BASE = 7000
COSTO_METRO = 200
IVA = 21
bonificacion = 0
recargo = 0

subtotal_consumo = consumo * COSTO_METRO
subtotal_factura = subtotal_consumo + TARIFA_BASE

match cliente:
    case "R":
        if consumo < 30:
            bonificacion = 10

        elif consumo > 80:
            recargo = 15

        if subtotal_consumo < 35000:
            bonificacion += 5

    case "C":
        if consumo > 300:
            bonificacion = 12
        
        elif consumo > 150:
            bonificacion = 8
        
        elif consumo < 50:
            recargo = 5        

    case "I":
        if consumo < 200:
            recargo = 10

        elif consumo > 1000:
            bonificacion = 30

        elif consumo > 500:
            bonificacion = 20


saldo_bonificar = subtotal_consumo * bonificacion/100
saldo_recargo = subtotal_consumo * recargo/100

subtotal = subtotal_factura - saldo_bonificar + saldo_recargo
recargo_iva = subtotal * IVA/100
total = subtotal + recargo_iva

print(f"El subtotal por lo consumido es: ${subtotal_consumo}")
print(f"Se aplicó una bonificación de: %{bonificacion}. El saldo a bonificar es de: ${saldo_bonificar}")
print(f"Se aplicó un recargo de: %{recargo}. El saldo de recargo es de: ${saldo_recargo}")
print(f"El subtotal junto a recargos y bonificaciones es de: ${subtotal}")
print(f"IVA aplicado: %{IVA}. Cargo aplicado por IVA: ${recargo_iva}")
print(f"El total a pagar es de: ${total}")

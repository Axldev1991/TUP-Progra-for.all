import random
import piedra_papel_tijera_utils

####### 1
def verificar_ganador_ronda(jugador, maquina) -> str:
    if (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    elif jugador == maquina:
        return "Empate"
    else:
        return "Máquina"

####### 2
def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        estado_partida = False
    elif ronda_actual > 3 and (aciertos_jugador != aciertos_maquina):
        estado_partida = False
    else:
        estado_partida = True
    return estado_partida

####### 3
def verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str:
    if aciertos_jugador > aciertos_maquina:
        return "JUGADOOOOOOR"
    return "MAQUINAAAAAAA"

####### 4
def mostrar_elemento(eleccion) -> str:
    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"

####### 5
def jugar_piedra_papel_tijera () -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    empates_totales = 0
    ronda_actual = 0
    
    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):
        while True:
            jugador = input("Haga su elección: Piedra (1) - Papel (2) - Tijera (3)")
            if jugador.isdigit() == True:
                jugador = int(jugador)
                if jugador >= 1 and jugador <= 3:
                    break
            print("mensaje de error")

        maquina = 3 #random.randint(1, 3)

        ronda_actual += 1
        print(f"RONDA N°: {ronda_actual}")
        print(mostrar_elemento(jugador))
        print(mostrar_elemento(maquina))

        resultado = verificar_ganador_ronda(jugador, maquina)

        if resultado == "Jugador":
            aciertos_jugador += 1
            print(f"gana {resultado}")
        elif resultado == "Máquina":
            aciertos_maquina += 1
            print(f"gana {resultado}")
        else:
            print("EMPATE")
            empates_totales += 1
    
    print(verificar_ganador_partida(aciertos_jugador, aciertos_maquina))


jugar_piedra_papel_tijera()



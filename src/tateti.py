from src.tablero import Tablero
from src.jugador import Jugador
from src.CLI import pedir_posicion, mostrar_mensaje

def jugar(movimientos=None):
    tablero = Tablero()
    jugador1 = Jugador("Jugador 1", "X")
    jugador2 = Jugador("Jugador 2", "O")
    jugadores = [jugador1, jugador2]

    turno = 0
    max_turnos = jugador1.max_fichas + jugador2.max_fichas  # 6 turnos

    while turno < max_turnos:
        jugador_actual = jugadores[turno % 2]
        tablero.mostrar()
        mostrar_mensaje(f"Turno de {jugador_actual.nombre} ({jugador_actual.ficha}). Fichas puestas: {jugador_actual.fichas_colocadas}/{jugador_actual.max_fichas}")

        if movimientos:
            fila, columna = movimientos[turno]
        else:
            fila, columna = pedir_posicion()

        if tablero.colocar_ficha(fila, columna, jugador_actual.ficha):
            jugador_actual.colocar_ficha()
            if tablero.verificar_ganador(jugador_actual.ficha):
                tablero.mostrar()
                mostrar_mensaje(f"¡{jugador_actual.nombre} gana!")
                return jugador_actual.ficha  # Retornamos ficha ganadora
            turno += 1
        else:
            mostrar_mensaje("Casilla ocupada, intenta de nuevo.")

    tablero.mostrar()
    mostrar_mensaje("¡Empate! Se colocaron todas las fichas sin ganador.")
    return "Empate"

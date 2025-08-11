class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

    def mostrar(self):
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 5)

    def colocar_ficha(self, fila, columna, ficha):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = ficha
            return True
        return False

    def verificar_ganador(self, ficha):
        # filas
        for fila in self.tablero:
            if all(c == ficha for c in fila):
                return True
        # columnas
        for col in range(3):
            if all(self.tablero[fila][col] == ficha for fila in range(3)):
                return True
        # diagonales
        if all(self.tablero[i][i] == ficha for i in range(3)):
            return True
        if all(self.tablero[i][2 - i] == ficha for i in range(3)):
            return True
        return False

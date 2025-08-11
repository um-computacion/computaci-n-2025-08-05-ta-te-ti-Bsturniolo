import unittest
from src.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_colocar_ficha(self):
        self.assertTrue(self.tablero.colocar_ficha(0, 0, "X"))
        self.assertFalse(self.tablero.colocar_ficha(0, 0, "O"))  # casilla ocupada

    def test_verificar_ganador_fila(self):
        self.tablero.tablero[0] = ["X", "X", "X"]
        self.assertTrue(self.tablero.verificar_ganador("X"))

    def test_verificar_ganador_columna(self):
        for i in range(3):
            self.tablero.tablero[i][1] = "O"
        self.assertTrue(self.tablero.verificar_ganador("O"))

    def test_verificar_ganador_diagonal(self):
        for i in range(3):
            self.tablero.tablero[i][i] = "X"
        self.assertTrue(self.tablero.verificar_ganador("X"))

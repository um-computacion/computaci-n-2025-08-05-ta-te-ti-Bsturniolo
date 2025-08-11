import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_colocar_ficha(self):
        jugador = Jugador("Test", "X")
        self.assertTrue(jugador.puede_colocar())
        for _ in range(3):
            self.assertTrue(jugador.colocar_ficha())
        self.assertFalse(jugador.puede_colocar())
        self.assertFalse(jugador.colocar_ficha())


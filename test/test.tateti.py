import unittest
from src.tateti import jugar

class TestTateti(unittest.TestCase):
    def test_ganador_x(self):
        movimientos = [
            (0,0),  # X
            (1,0),  # O
            (0,1),  # X
            (1,1),  # O
            (0,2),  # X gana con fila 0
            (2,2)   # O (no se juega porque gana X antes)
        ]
        resultado = jugar(movimientos)
        self.assertEqual(resultado, "X")

    def test_empate(self):
        movimientos = [
            (0,0),  # X
            (0,1),  # O
            (0,2),  # X
            (1,0),  # O
            (1,1),  # X
            (2,0),  # O - todas fichas puestas, sin ganador
        ]
        resultado = jugar(movimientos)
        self.assertEqual(resultado, "Empate")

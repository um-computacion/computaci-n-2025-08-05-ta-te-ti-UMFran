import unittest
from src.jugador import Jugador


class TestJugador(unittest.TestCase):
    
    def test_init_nombre_y_ficha(self):
        jugador = Jugador("Ana", "X")
        self.assertEqual(jugador.nombre, "Ana")
        self.assertEqual(jugador.ficha, "X")
    
    def test_init_con_ficha_o(self):
        jugador = Jugador("Franco", "O")
        self.assertEqual(jugador.nombre, "Franco")
        self.assertEqual(jugador.ficha, "O")
    
    def test_init_con_nombres_diferentes(self):
        jugador1 = Jugador("Mario", "X")
        jugador2 = Jugador("Pedro", "O")
        self.assertEqual(jugador1.nombre, "Mario")
        self.assertEqual(jugador2.nombre, "Pedro")
        self.assertNotEqual(jugador1.nombre, jugador2.nombre)
    
    def test_init_con_fichas_diferentes(self):
        jugador1 = Jugador("Luis", "X")
        jugador2 = Jugador("José", "O")
        self.assertEqual(jugador1.ficha, "X")
        self.assertEqual(jugador2.ficha, "O")
        self.assertNotEqual(jugador1.ficha, jugador2.ficha)
    
    def test_str_representation(self):
        jugador = Jugador("Sofia", "X")
        expected = "Jugador: Sofia ficha: X"
        self.assertEqual(str(jugador), expected)
    
    def test_atributos_modificables(self):
        jugador = Jugador("Juan", "X")
        jugador.nombre = "Pedro"
        jugador.ficha = "O"
        self.assertEqual(jugador.nombre, "Pedro")
        self.assertEqual(jugador.ficha, "O")
    
    def test_igualdad_objetos_mismo_nombre_ficha(self):
        jugador1 = Jugador("Roberto", "X")
        jugador2 = Jugador("Roberto", "X")
        self.assertNotEqual(jugador1, jugador2)
        self.assertIsNot(jugador1, jugador2)


if __name__ == '__main__':
    unittest.main()
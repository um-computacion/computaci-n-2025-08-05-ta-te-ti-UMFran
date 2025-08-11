import unittest
from src.tablero import Tablero, PosOcupadaException, CasillaFueradeRango

class TestTablero(unittest.TestCase):
    
    def test_init(self):
        tablero = Tablero()
        contenedor = tablero.contenedor
        self.assertEqual(len(contenedor), 3)
        self.assertEqual(contenedor[0], ["","",""])
    
    def test_poner_ficha_valida(self):
        tablero = Tablero()
        tablero.poner_la_ficha(1, 1, "X")
        self.assertEqual(tablero.obtener_contenedor()[1][1], "X")
    
    def test_poner_ficha_fila_fuera_de_rango_negativa(self):
        tablero = Tablero()
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(-1, 0, "X")

    def test_poner_ficha_fila_fuera_de_rango_alta(self):
        tablero = Tablero()
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(3, 0, "X")

    def test_poner_ficha_columna_fuera_de_rango_negativa(self):
        tablero = Tablero()
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(0, -1, "X")

    def test_poner_ficha_columna_fuera_de_rango_alta(self):
        tablero = Tablero()
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(0, 3, "X")

    def test_poner_ficha_ambas_coordenadas_fuera_de_rango(self):
        tablero = Tablero()
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(-1, -1, "X")
        
        with self.assertRaises(CasillaFueradeRango):
            tablero.poner_la_ficha(5, 5, "O")
    
    def test_poner_ficha_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_la_ficha(1, 1, "X")

        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(1, 1, "O")

    def test_poner_ficha_multiple_posiciones_ocupadas(self):
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        tablero.poner_la_ficha(0, 1, "O")
        tablero.poner_la_ficha(2, 2, "X")
        
        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(0, 0, "O")
        
        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(0, 1, "X")
        
        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(2, 2, "O")
    
    def test_esta_lleno_false(self):
        tablero = Tablero()
        self.assertFalse(tablero.esta_lleno())
    
    def test_esta_lleno_true(self):
        tablero = Tablero()
        for fila in range(3):
            for col in range(3):
                tablero.poner_la_ficha(fila, col, "X")
        self.assertTrue(tablero.esta_lleno())

if __name__ == '__main__':
    unittest.main()
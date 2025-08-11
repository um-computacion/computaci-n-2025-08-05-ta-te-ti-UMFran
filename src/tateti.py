from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, jugador1 = Jugador, jugador2 = Jugador): 
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = self.jugador1
        self.tablero = Tablero()

    def condicion_ganar(self, ficha):
        for fila in self.tablero.contenedor:
            if all(celda == ficha for celda in fila):
                return True
        
        for columna in range(3):
            if all(self.tablero.contenedor[fila][columna] == ficha for fila in range(3)):
                return True
        
        if all(self.tablero.contenedor[i][i] == ficha for i in range(3)):
            return True

        if all(self.tablero.contenedor[i][2 - i] == ficha for i in range(3)):
            return True
        
        return False

    def ocupar_una_de_las_casillas(self, fil, col):
        # pongo la ficha...
        self.tablero.poner_la_ficha(fil, col, self.turno.ficha)
        
    def cambiar_turno(self):
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1
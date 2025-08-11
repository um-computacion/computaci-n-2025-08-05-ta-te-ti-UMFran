class PosOcupadaException(Exception):
    ...

class CasillaFueradeRango(Exception):
    ...

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]


    def poner_la_ficha(self, fil, col, ficha):
        if fil < 0 or fil > 2 or col < 0 or col > 2:
            raise CasillaFueradeRango("fila o columna fuera de rango")
        
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
    
    def esta_lleno(self):
        for fila in self.contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        return True
    
    def reiniciar_tablero(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
    
    def tablero(self):
        for fila in self.contenedor:
            print (fila)
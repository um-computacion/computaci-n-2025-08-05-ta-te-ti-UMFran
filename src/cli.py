from src.tateti import Tateti
from src.jugador import Jugador
from src.tablero import PosOcupadaException, CasillaFueradeRango

def main():
    print("Bienvenidos al Tateti")
    nombre_1 = str(input("Ingrese el nombre del primer jugador (ficha X): "))
    nombre_2 = str(input("Ingrese el nombre del segundo jugador (ficha 0): "))
    jugador_1 = Jugador(nombre_1, "X")
    jugador_2 = Jugador(nombre_2, "O")
    juego = Tateti(jugador_1, jugador_2)

    while True:
        print("-------------------------------------------------------")
        print("Tablero: ")
        print(juego.tablero.tablero())
        print(f"Turno de {juego.turno.nombre}, ficha: {juego.turno.ficha} ")
        try:
            fil = int(input("Ingrese fila"))
            col = int(input("Ingrese col"))
            juego.ocupar_una_de_las_casillas(fil, col)
            print("Ficha puesta")

            if juego.condicion_ganar(juego.turno.ficha):
                juego.tablero.tablero()
                print(f"El ganador es {juego.turno.ficha}")
                break
            elif juego.tablero.esta_lleno():
                juego.tablero.tablero()
                print("El juego ha terminado en empate")
                break
        
            juego.cambiar_turno()

        except CasillaFueradeRango as e:
            print("Esta casilla esta fuera de rango. Elije una entre 0 y 2")
        except PosOcupadaException as e:
            print("Esta casilla ya esta ocupada. Elije otra")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
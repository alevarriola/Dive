# definimos dos nueva funcion, seria nuestro turno de pacman
# le damos a pacman la capadidad de moverse en el terrero disponible
# a pacman lo manejaremos nosotros
# primera funcion, verificar que el movimiento este dentro del tablero (es valido)
# segunda funcion, realizar el movimiento y si es valido romper el ciclo/turno


class Juego:

    def __init__(self):
        self.tablero = [["🔲" for _ in range(10)] for _ in range(10)]
        
        self.pacman = (0,0)
        self.fantasma = (9,9)

        self.turno = 0
        self.turno_max = 20

    def actualizar_tablero(self):
        self.tablero = [["🔲" for _ in range(10)] for _ in range(10)]
        self.tablero[self.pacman[0]][self.pacman[1]] = "🟡"
        self.tablero[self.fantasma[0]][self.fantasma[1]] = "👾"

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))

    def movimientos_validos_pacman(self, posicion):
        if not (0 <= posicion[0] < 10 and 0 <= posicion[1] < 10):
            return False
        return True
    
    def movimiento_pacman(self):
        while True:
            direccion = input('Ingrese una direccion (W,A,S,D)')
            if direccion == 'w':
                nueva_direccion = (self.pacman[0] - 1, self.pacman[1])
            elif direccion == 's':
                nueva_direccion = (self.pacman[0] + 1, self.pacman[1])
            elif direccion == 'a':
                nueva_direccion = (self.pacman[0], self.pacman[1] - 1)
            elif direccion == 'd':
                nueva_direccion = (self.pacman[0], self.pacman[1] + 1)
            else:
                print('Direccion no valida, recuerde (W,A,S,D)')
                continue

            if self.movimientos_validos_pacman(nueva_direccion):
                self.pacman = nueva_direccion

                # a fines de demostracion, esto no deberia ir aqui
                self.actualizar_tablero()
                self.imprimir_tablero()

                # aqui deberia solo romperse el ciclo dando por terminado el turno
                #break

            else:
                print('Movimiento no valido')

            





play = Juego()

play.actualizar_tablero()
play.imprimir_tablero()

play.movimiento_pacman()
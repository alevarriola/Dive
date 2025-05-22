# hacemos el tablero, ubicamos a Pacman y el fantasma, definimos candidades de turno y creamos 2 funciones
# primera funcion para actualizar nuestro tablero cada vez que requerimos con la posicion real de pacman y el fantasma
# segunda funcion para imprimir linea por linea lo que se encuentra guardado en self.tablero

class Juego:

    def __init__(self):
        self.tablero = [["🔲" for _ in range(10)] for _ in range(10)]
        
        #el primer dato seria eje Y(columna), el segundo eje X(fila)
        self.pacman = (0,0) 
        self.fantasma = (9,9)

        self.turno = 0
        self.turno_max = 20

    def actualizar_tablero(self):
        self.tablero = [["🔲" for _ in range(10)] for _ in range(10)]
        self.tablero[self.pacman[0]] [self.pacman[1]] = "🟡"
        self.tablero[self.fantasma[0]] [self.fantasma[1]] = "👾"

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))

play = Juego()

play.actualizar_tablero()
play.imprimir_tablero()

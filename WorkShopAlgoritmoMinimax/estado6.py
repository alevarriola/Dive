# tercera y ultima parte del algoritmo del movimiento del fantasma
# implementaremos minimax
# dios nos bendiga a todos

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
                break

            else:
                print('Movimiento no valido')

    def verificar_victoria(self):
        if self.pacman == self.fantasma:
            return "Fantasma"
        if self.turno >= self.turno_max:
            return "Pacman"
        return None
    
    def jugar_turno(self):
        self.movimiento_pacman()

        resultado = self.verificar_victoria()
        if resultado == "Fantasma":
            print("¡El Fantasma atrapó a Pac-Man!")
            return
        elif resultado == "Pacman":
            print("¡Pac-man escapó del fantasma!")
            return

        self.movimiento_fantasma()
        self.turno = self.turno + 1

        resultado = self.verificar_victoria()
        if resultado == "Fantasma":
            print("¡El Fantasma atrapó a Pac-Man!")
            return
        elif resultado == "Pacman":
            print("¡Pac-man escapó del fantasma!")
            return

    def movimiento_valido_fantasma(self, posicion=None):
        if posicion == None:
            posicion = self.fantasma

        direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
        posibles = []

        for movimiento in direcciones:
            nueva_posicion_ejey = posicion[0] + movimiento[0]
            nueva_posicion_ejex = posicion[1] + movimiento[1]
            if 0 <= nueva_posicion_ejey < 10 and 0 <= nueva_posicion_ejex < 19:
                posibles.append((nueva_posicion_ejey, nueva_posicion_ejex))

        return posibles


    def movimiento_fantasma(self):
        posicion_pacman = self.pacman
        mejor_movimiento = self.get_mejor_movimiento(posicion_pacman) 

        if mejor_movimiento:
            self.fantasma = mejor_movimiento

    def get_mejor_movimiento(self, posicion_pacman):
        mejor_puntaje = float('-inf')
        mejor_movimiento = None

        for movimiento in self.movimiento_valido_fantasma():

            backup_pos_fantasma = self.fantasma
            self.fantasma = movimiento

            puntaje = self.minimax(0, True, movimiento, posicion_pacman)

            self.fantasma = backup_pos_fantasma

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento
        
        return mejor_movimiento
    
    def evaluar_puntaje(self, posicion_fantasma, posicion_pacman):
        if posicion_fantasma == posicion_pacman:
            return 100
        if self.turno >= self.turno_max:
            return -100
        
        distancia_ejey = abs(posicion_pacman[0] - posicion_fantasma[0])
        distancia_ejex = abs(posicion_pacman[1] - posicion_fantasma[1])

        return -(distancia_ejey + distancia_ejex)
    
    def minimax(self, profundidad, es_maximizador, posicion_fantasma, posicion_pacman):

        if profundidad == 5 or posicion_fantasma == posicion_pacman or self.turno + profundidad >= self.turno_max:
            return self.evaluar_puntaje(posicion_fantasma, posicion_pacman)
        
        if es_maximizador:
            mejor_puntaje = float('-inf')
            for movimiento in self.movimiento_valido_fantasma(posicion_fantasma):

                puntaje = self.minimax(profundidad + 1, False, movimiento, posicion_pacman)
                mejor_puntaje = max(mejor_puntaje, puntaje)
            
            return mejor_puntaje
        
        else:
            peor_puntaje = float('inf')
            for movimiento in self.movimiento_valido_fantasma(posicion_pacman):

                puntaje = self.minimax(profundidad + 1, True, posicion_fantasma, movimiento)
                peor_puntaje = min(peor_puntaje, puntaje)

            return peor_puntaje



play = Juego()

play.actualizar_tablero()
play.imprimir_tablero()

while True:
    play.jugar_turno()
    play.actualizar_tablero()

    print(f'Turno: {play.turno}')
    play.imprimir_tablero()

    resultado = play.verificar_victoria()
    if resultado:
        print(f"¡Ganador: {resultado}!")
        break

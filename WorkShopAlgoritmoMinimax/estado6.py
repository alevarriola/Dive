# tercera y ultima parte del algoritmo del movimiento del gato
# implementaremos minimax
# dios nos bendiga a todos

class Juego:

    def __init__(self):
        self.tablero = [["⬜" for _ in range(10)] for _ in range(10)]
        
        self.raton = (0,0)
        self.gato = (9,9)

        self.turno = 0
        self.turno_max = 20

    def actualizar_tablero(self):
        self.tablero = [["⬜" for _ in range(10)] for _ in range(10)]
        self.tablero[self.raton[0]][self.raton[1]] = "🐭"
        self.tablero[self.gato[0]][self.gato[1]] = "😾"

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))

    def movimientos_validos_raton(self, posicion):
        if not (0 <= posicion[0] < 10 and 0 <= posicion[1] < 10):
            return False
        return True
    
    def movimiento_raton(self):
        while True:
            direccion = input('Ingrese una direccion (W,A,S,D)')
            if direccion == 'w':
                nueva_direccion = (self.raton[0] - 1, self.raton[1])
            elif direccion == 's':
                nueva_direccion = (self.raton[0] + 1, self.raton[1])
            elif direccion == 'a':
                nueva_direccion = (self.raton[0], self.raton[1] - 1)
            elif direccion == 'd':
                nueva_direccion = (self.raton[0], self.raton[1] + 1)
            else:
                print('Direccion no valida, recuerde (W,A,S,D)')
                continue

            if self.movimientos_validos_raton(nueva_direccion):
                self.raton = nueva_direccion
                break

            else:
                print('Movimiento no valido')

    def verificar_victoria(self):
        if self.raton == self.gato:
            return "Gato"
        if self.turno >= self.turno_max:
            return "Raton"
        return None
    
    def jugar_turno(self):
        self.movimiento_raton()

        resultado = self.verificar_victoria()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return

        self.movimiento_gato()

        resultado = self.verificar_victoria()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
        self.turno = self.turno + 1

    def movimiento_valido_gato(self, posicion=None):
        if posicion == None:
            posicion = self.gato

        direcciones = [(-1,0), (1,0), (0,-1), (0,1)]
        posibles = []

        for movimiento in direcciones:
            nueva_posicion_ejey = posicion[0] + movimiento[0]
            nueva_posicion_ejex = posicion[1] + movimiento[1]
            if 0 <= nueva_posicion_ejey < 10 and 0 <= nueva_posicion_ejex < 19:
                posibles.append((nueva_posicion_ejey, nueva_posicion_ejex))

        return posibles


    def movimiento_gato(self):
        posicion_raton = self.raton
        mejor_movimiento = self.get_mejor_movimiento(posicion_raton) 

        if mejor_movimiento:
            self.gato = mejor_movimiento

    def get_mejor_movimiento(self, posicion_raton):
        mejor_puntaje = float('-inf')
        mejor_movimiento = None

        for movimiento in self.movimiento_valido_gato():

            backup_pos_gato = self.gato
            self.gato = movimiento

            puntaje = self.minimax(0, True, movimiento, posicion_raton)

            self.gato = backup_pos_gato

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento
        
        return mejor_movimiento
    
    def evaluar_puntaje(self, posicion_gato, posicion_raton):
        if posicion_gato == posicion_raton:
            return 100
        if self.turno >= self.turno_max:
            return -100
        
        distancia_ejey = abs(posicion_raton[0] - posicion_gato[0])
        distancia_ejex = abs(posicion_raton[1] - posicion_gato[1])

        return -(distancia_ejey + distancia_ejex)
    
    def minimax(self, profundidad, es_maximizador, posicion_gato, posicion_raton):

        if profundidad == 5 or posicion_gato == posicion_raton or self.turno + profundidad >= self.turno_max:
            return self.evaluar_puntaje(posicion_gato, posicion_raton)
        
        if es_maximizador:
            mejor_puntaje = float('-inf')
            for movimiento in self.movimiento_valido_gato(posicion_gato):

                puntaje = self.minimax(profundidad + 1, False, movimiento, posicion_raton)
                mejor_puntaje = max(mejor_puntaje, puntaje)
            
            return mejor_puntaje
        
        else:
            peor_puntaje = float('inf')
            for movimiento in self.movimiento_valido_gato(posicion_raton):

                puntaje = self.minimax(profundidad + 1, True, posicion_gato, movimiento)
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

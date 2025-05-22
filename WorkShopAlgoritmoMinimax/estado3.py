# añadiremos una condicion de victoria y empezar un turno
# cuando se cumpla la condicion de virtoria el juego finaliza 

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

        #self.movimiento_gato()  aun no definido

        resultado = self.verificar_victoria()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
        self.turno = self.turno + 1





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


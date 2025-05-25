# Importamos todas nuestras clases para usarlas en una clase general que sera la logica de nuestro juego
from tablero import Tablero
from players import Cat, Mouse
from object import Wall, Cheese

class MouseVsCat:

    # definimos en nuestro init todos nuestros elementos usando sus clases
    def __init__(self, ejex_mouse, ejey_mouse, ejex_cat, ejey_cat, ejex_cheese, ejey_cheese, tamaño, cant_walls):
        self.tablero = Tablero(tamaño)
        self.mouse = Mouse(ejex_mouse, ejey_mouse)  
        self.cat = Cat(ejex_cat, ejey_cat)
        self.cheese = Cheese(ejex_cheese, ejey_cheese)
        self.walls = [] #lista vacia para rellenar con ubicaciones de obstaculos

        self.cant_walls = cant_walls 
        self.turnos = 0 
        self.max_turno = 100

        # funcion para spawnear obstaculos, mientras no haya la cantidad definida
        while len(self.walls) < self.cant_walls:
            
            wall = Wall(tamaño)
            # verinifamos si no esta el raton, el gato, el queso u otro obstaculo en la posicion
            ocupado = (
                (wall.ejex, wall.ejey) == (self.mouse.ejex, self.mouse.ejey) or
                (wall.ejex, wall.ejey) == (self.cat.ejex, self.cat.ejey) or
                (wall.ejex, wall.ejey) == (self.cheese.ejex, self.cheese.ejey) or
                any((wall.ejex, wall.ejey) == (w.ejex, w.ejey) for w in self.walls)
            )
            # si no esta ocupado
            if not ocupado:
                self.walls.append(wall) 

    # funcion para que nunca dupliquemos entidades
    def actualizar_tablero(self):
        #tablero en blanco
        self.tablero.reset() 

        # ubicamos nuestros queso, raton y gato con su imagen
        self.tablero.tablero[self.cheese.ejey][self.cheese.ejex] = self.cheese.img 
        self.tablero.tablero[self.mouse.ejey][self.mouse.ejex] = self.mouse.img 
        self.tablero.tablero[self.cat.ejey][self.cat.ejex] = self.cat.img 

        for wall in self.walls:
            self.tablero.tablero[wall.ejey][wall.ejex] = wall.img #por cada pared, la ubicamos en su posicion

        if self.mouse.ejex == self.cat.ejex and self.mouse.ejey == self.cat.ejey:
             self.tablero.tablero[self.cat.ejey][self.cat.ejex] = '💥' #si el gato y raton estan en la misma ubicacion

        if self.mouse.ejex == self.cheese.ejex and self.mouse.ejey == self.cheese.ejey:
             self.tablero.tablero[self.cheese.ejey][self.cheese.ejex] = '🍴' #si el raton y queso estan en la misma ubicacion

    # funcion para saber quien es el ganador
    def check_winner(self):
        #Si el gato esta en la misma posicion del raton
        if self.mouse.ejex == self.cat.ejex and self.mouse.ejey == self.cat.ejey:
            return "Gato"
         
        #Si el raton esta en la misma posicion del queso o terminan los turnos
        if self.mouse.ejex == self.cheese.ejex and self.mouse.ejey == self.cheese.ejey:
            return "Raton" 
        if self.turnos >= self.max_turno:
            return "Raton" 
        
        return None #si nada se cumple, retornar vacio


    # definimos la logica de turnos para AI contra AI
    def jugar_turno_AI_vs_AI(self):

        self.cat.movimiento_AI(self.mouse, self.tablero, self.turnos, self.max_turno, self.cheese)
        self.mouse.movimiento_AI(self.cat, self.tablero, self.turnos, self.max_turno, self.cheese)      

        self.turnos = self.turnos + 1

        # actualizamos nuestro tablero con las nuevas posiciones x e y del gato y raton, y print de turnos
        self.actualizar_tablero()
        print(f"Turno #{self.turnos}") 

        #verificamos si hay un ganador, guardamos en una variable y verificamos si es que hay, quien es el ganador
        resultado = self.check_winner() 
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!") 
            return
        
    # definimos misma logica que el anterior, pero en este caso llamamos al movimiento del raton usuario
    def jugar_turno_MOU_vs_AI(self):

        self.cat.movimiento_AI(self.mouse, self.tablero, self.turnos, self.max_turno, self.cheese)
        self.mouse.movimiento_usuario(self.tablero) # en vez de self.mouse.movimientoAI

        self.turnos = self.turnos + 1

        self.actualizar_tablero()
        print(f"Turno #{self.turnos}")

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
     # movimiento del gato usuario
    def jugar_turno_CAT_vs_AI(self):

        self.mouse.movimiento_AI(self.cat, self.tablero, self.turnos, self.max_turno, self.cheese)   
        self.cat.movimiento_usuario(self.tablero)

        self.turnos = self.turnos + 1

        self.actualizar_tablero()
        print(f"Turno #{self.turnos}")

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return

    # modo de juego paseo por el campo, movimiento aleatorio
    def jugar_turno_MOU_vs_RD(self):

        self.cat.movimiento_aleatorio(self.tablero)
        self.mouse.movimiento_usuario(self.tablero) 
        self.turnos = self.turnos + 1

        self.actualizar_tablero()
        print(f"Turno #{self.turnos}")

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
     # movimiento del gato usuario
    def jugar_turno_CAT_vs_RD(self):

        self.mouse.movimiento_aleatorio(self.tablero)
        self.cat.movimiento_usuario(self.tablero)

        self.turnos = self.turnos + 1

        self.actualizar_tablero()
        print(f"Turno #{self.turnos}")

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return

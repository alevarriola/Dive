from tablero import Tablero
from players import Cat, Mouse
from object import Wall, Cheese

class MouseVsCat:

    def __init__(self, ejex_mouse, ejey_mouse, ejex_cat, ejey_cat):
        self.tablero = Tablero()
        self.mouse = Mouse(ejex_mouse, ejey_mouse)  
        self.cat = Cat(ejex_cat, ejey_cat)
        self.cheese = Cheese()
        self.walls = []

        self.cant_walls = 5
        self.turnos = 0
        self.max_turno = 100

        while len(self.walls) < self.cant_walls:
            wall = Wall()
            ocupado = (
                (wall.ejex, wall.ejey) == (self.mouse.ejex, self.mouse.ejey) or
                (wall.ejex, wall.ejey) == (self.cat.ejex, self.cat.ejey) or
                (wall.ejex, wall.ejey) == (self.cheese.ejex, self.cheese.ejey) or
                any((wall.ejex, wall.ejey) == (w.ejex, w.ejey) for w in self.walls)
            )
            if not ocupado:
                self.walls.append(wall)

    def jugar_turno_AI_vs_AI(self):

        self.mouse.movimiento_AI(self.cat, self.tablero, self.turnos, self.max_turno, self.cheese)

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
        self.cat.movimiento_AI(self.mouse, self.tablero, self.turnos, self.max_turno, self.cheese)

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
        
    def jugar_turno_RD_vs_AI(self):

        self.mouse.movimiento_aleatorio(self.tablero)

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return

        self.cat.movimiento_AI(self.mouse, self.tablero, self.turnos, self.max_turno, self.cheese)

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
        
    def jugar_turno_PY_vs_AI(self):

        self.mouse.movimiento_usuario(self.tablero)

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return

        self.cat.movimiento_AI(self.mouse, self.tablero, self.turnos, self.max_turno, self.cheese)

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


    def actualizar_tablero(self):
        self.tablero.reset()
        self.tablero.tablero[self.cheese.ejey][self.cheese.ejex] = self.cheese.img
        self.tablero.tablero[self.mouse.ejey][self.mouse.ejex] = self.mouse.img
        self.tablero.tablero[self.cat.ejey][self.cat.ejex] = self.cat.img

        for wall in self.walls:
            self.tablero.tablero[wall.ejey][wall.ejex] = wall.img

        if self.mouse.ejex == self.cat.ejex and self.mouse.ejey == self.cat.ejey:
             self.tablero.tablero[self.cat.ejey][self.cat.ejex] = '🍴'

    def check_winner(self):
        if self.mouse.ejex == self.cat.ejex and self.mouse.ejey == self.cat.ejey:
            return "Gato"
        
        if self.mouse.ejex == self.cheese.ejex and self.mouse.ejey == self.cheese.ejey:
            return "Raton"
        if self.turnos >= self.max_turno:
            return "Raton"
        
        return None
   
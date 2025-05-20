from tablero import Tablero
from players import Cat, Mouse

class MouseVsCat:

    def __init__(self):
        self.tablero = Tablero()
        self.mouse = Mouse(4, 4)  
        self.cat = Cat(9, 9)     
        self.tablero.tablero[4][4] = '🐀'
        self.tablero.tablero[9][9] = '😾'
        self.turnos = 0

    def jugar_turno(self):

        self.mouse.movimiento_IA(self.get_best_move_mouse)

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
        self.cat.movimiento(self.get_best_move_cat)
        self.turnos = self.turnos + 1

        resultado = self.check_winner()
        if resultado == "Gato":
            print("¡El gato atrapó al ratón!")
            return
        elif resultado == "Raton":
            print("¡El ratón escapó del gato!")
            return
        
        self.actualizar_tablero()
        print(f"Turno #{self.turnos}")

    def actualizar_tablero(self):
        self.tablero.reset()
        self.tablero.tablero[self.mouse.ejey][self.mouse.ejex] = '🐀'
        self.tablero.tablero[self.cat.ejey][self.cat.ejex] = '😾'

    def check_winner(self):
        if self.mouse.ejex == self.cat.ejex and self.mouse.ejey == self.cat.ejey:
            return "Gato"
        if self.turnos >= 20:
            return "Raton"
        return None
    
    def evaluar_estado(self, cat_pos, mouse_pos):
        if mouse_pos[0] == cat_pos[0] and mouse_pos[1] == cat_pos[1]:
            return 100  
        if self.turnos >= 20:
            return -100
        
        dx = abs(mouse_pos[0] - cat_pos[0])
        dy = abs(mouse_pos[1] - cat_pos[1])
        return -(2 * (dx + dy) + self.turnos)
    
    def movimientos_validos(self, pos):
        DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        posibles = []

        for dx, dy in DIRECCIONES:
            nuevo_x = pos[0] + dx
            nuevo_y = pos[1] + dy
            if 0 <= nuevo_x < 10 and 0 <= nuevo_y < 10:
                if self.tablero.tablero[nuevo_y][nuevo_x] != '❌':
                    posibles.append((nuevo_x, nuevo_y))

        return posibles

    def get_best_move_cat(self):
        best_score = float("-inf")
        best_move = None
        current_pos = (self.cat.ejex, self.cat.ejey)
        mouse_pos = (self.mouse.ejex, self.mouse.ejey)

        for move in self.movimientos_validos(current_pos):

            old_cat_pos = (self.cat.ejex, self.cat.ejey)
            self.cat.ejex, self.cat.ejey = move

            score = self.minimax(0, True, move, mouse_pos)

            if move == self.cat.ultimo_movimiento:
                score -= 5

            self.cat.ejex, self.cat.ejey = old_cat_pos

            if score > best_score:
                best_score = score
                best_move = move

        return best_move
    
    def get_best_move_mouse(self):
        best_score = float("-inf")
        best_move = None
        current_pos = (self.mouse.ejex, self.mouse.ejey)
        cat_pos = (self.cat.ejex, self.cat.ejey)

        for move in self.movimientos_validos(current_pos):

            old_mouse_pos = (self.mouse.ejex, self.mouse.ejey)
            self.mouse.ejex, self.mouse.ejey = move

            score = self.minimax(0, False, move, cat_pos)


            self.mouse.ejex, self.mouse.ejey = old_mouse_pos

            if score > best_score:
                best_score = score
                best_move = move

        return best_move
    
    def minimax(self, profundidad, es_maximizador, cat_pos=None, mouse_pos=None):
        

        if cat_pos is None:
            cat_pos = (self.cat.ejex, self.cat.ejey)
        if mouse_pos is None:
            mouse_pos = (self.mouse.ejex, self.mouse.ejey)
        
        if profundidad == 5 or cat_pos == mouse_pos or self.turnos + profundidad >= 20:
            return self.evaluar_estado(cat_pos, mouse_pos)

        if es_maximizador:
            max_eval = float("-inf")
            
            for move in self.movimientos_validos(cat_pos):
                eval = self.minimax(profundidad + 1, False, move, mouse_pos)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            
            for move in self.movimientos_validos(mouse_pos):
                eval = self.minimax(profundidad + 1, True, cat_pos, move)
                min_eval = min(min_eval, eval)
            return min_eval
    
   
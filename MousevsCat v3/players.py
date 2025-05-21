import random

class Cat:

    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
      
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.img = "😾"
        self.ultimos_movimientos = []
    
    def movimientos_validos(self, tablero, pos=None):

        if pos == None:
            pos = (self.ejex, self.ejey) 

        posibles = []

        for dx, dy in self.DIRECCIONES:
            nuevo_x = pos[0] + dx
            nuevo_y = pos[1] + dy
            if 0 <= nuevo_x < 10 and 0 <= nuevo_y < 10:
                if tablero.tablero[nuevo_y][nuevo_x] != '❌':
                    posibles.append((nuevo_x, nuevo_y))

        return posibles

    def movimiento_AI (self, mouse_pos, tablero, turno, max_turno, cheese_pos):

        mouse_pos = (mouse_pos.ejex, mouse_pos.ejey)
        cheese_pos = (cheese_pos.ejex, cheese_pos.ejey)
        mejor_movimiento = self.get_best_move(mouse_pos, tablero, turno, max_turno, cheese_pos)
        
        if mejor_movimiento:
            self.ejex, self.ejey = mejor_movimiento
           
            self.ultimos_movimientos.append(mejor_movimiento)
            if len(self.ultimos_movimientos) > 4:
                self.ultimos_movimientos.pop(0)

    def get_best_move(self, mouse_pos, tablero, turno, max_turno, cheese_pos):
        best_score = float("-inf")
        best_move = None

        for move in self.movimientos_validos(tablero):

            old_cat_pos = (self.ejex, self.ejey)
            self.ejex, self.ejey = move

            score = self.minimax(0, True, move, mouse_pos, turno, max_turno, tablero, cheese_pos)

            if len(self.ultimos_movimientos) >= 2:
                if move in self.ultimos_movimientos:
                    score -= 5 

            self.ejex, self.ejey = old_cat_pos

            if score > best_score:
                best_score = score
                best_move = move

        return best_move   
    
    def evaluar_estado(self, cat_pos, mouse_pos, turno, max_turno, cheese_pos):
        if mouse_pos == cat_pos:
            return 1000  
        if turno >= max_turno:
            return -1000
        if mouse_pos == cheese_pos:
            return -1000
    
        dx = abs(mouse_pos[0] - cat_pos[0])
        dy = abs(mouse_pos[1] - cat_pos[1])
        return -(5*dx + 2*dy + turno)
    
    def minimax(self, profundidad, es_maximizador, cat_pos, mouse_pos, turno, max_turno, tablero, cheese_pos):
        
        if profundidad == 5 or cat_pos == mouse_pos or mouse_pos == cheese_pos or turno + profundidad >= max_turno:
                return self.evaluar_estado(cat_pos, mouse_pos, turno, max_turno, cheese_pos)

        if es_maximizador:
            max_eval = float("-inf")
            
            for move in self.movimientos_validos(tablero, mouse_pos):
                eval = self.minimax(profundidad + 1, False, cat_pos, move, turno, max_turno, tablero, cheese_pos)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            
            for move in self.movimientos_validos(tablero, cat_pos):
                eval = self.minimax(profundidad + 1, True, move, mouse_pos, turno, max_turno, tablero, cheese_pos)
                min_eval = min(min_eval, eval)
            return min_eval
    
   



class Mouse:

    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.img = "🐭"
        self.ultimos_movimientos = []
    
    def es_movimiento_valido(self, tablero, x, y):
        if not (0 <= x < 10 and 0 <= y < 10):
            return False
        if tablero.tablero[y][x] == '❌':
            return False
        return True


    def movimiento_aleatorio (self, tablero):
        direcciones = self.DIRECCIONES.copy()
        random.shuffle(direcciones)  


        for dx, dy in direcciones:
            nuevo_x = self.ejex + dx
            nuevo_y = self.ejey + dy

            if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                self.ejex = nuevo_x
                self.ejey = nuevo_y 
                break 

    def movimiento_usuario (self, tablero):

        while True:         
            direccion = input("Ingrese una direccion [W, A, S, D]").strip().lower()

            if direccion == "w":
                nuevo_x = self.ejex
                nuevo_y = self.ejey - 1
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "s":
                nuevo_x = self.ejex
                nuevo_y = self.ejey + 1
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "a":
                nuevo_x = self.ejex - 1
                nuevo_y = self.ejey
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "d":
                nuevo_x = self.ejex + 1
                nuevo_y = self.ejey
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    break
                else:
                    print("Movimiento no valido")

            else:
                print("Comando no reconocido, comandos validos [W, A, S, D]")


    def movimiento_AI (self, cat_pos, tablero, turno, max_turno, cheese_pos):

        cat_pos = (cat_pos.ejex, cat_pos.ejey)
        cheese_pos = (cheese_pos.ejex, cheese_pos.ejey)
        mejor_movimiento = self.get_best_move(cat_pos, tablero, turno, max_turno, cheese_pos)
        
        if mejor_movimiento:
            self.ejex, self.ejey = mejor_movimiento

            self.ultimos_movimientos.append(mejor_movimiento)
            if len(self.ultimos_movimientos) > 4:
                self.ultimos_movimientos.pop(0)

    def movimientos_validos(self, tablero, pos=None):

        if pos == None:
            pos = (self.ejex, self.ejey) 

        posibles = []

        for dx, dy in self.DIRECCIONES:
            nuevo_x = pos[0] + dx
            nuevo_y = pos[1] + dy
            if 0 <= nuevo_x < 10 and 0 <= nuevo_y < 10:
                if tablero.tablero[nuevo_y][nuevo_x] != '❌':
                    posibles.append((nuevo_x, nuevo_y))

        return posibles    

    def get_best_move(self, cat_pos, tablero, turno, max_turno, cheese_pos):
        best_score = float("-inf")
        best_move = None

        for move in self.movimientos_validos(tablero):

            old_mouse_pos = (self.ejex, self.ejey)
            self.ejex, self.ejey = move

            score = self.minimax(0, True, move, cat_pos, turno, max_turno, tablero, cheese_pos)

            if len(self.ultimos_movimientos) >= 2:
                if move in self.ultimos_movimientos:
                    score -= 5 

            self.ejex, self.ejey = old_mouse_pos

            if score > best_score:
                best_score = score
                best_move = move

        return best_move   

    def evaluar_estado(self, cat_pos, mouse_pos, turno, max_turno, cheese_pos):
        
        if mouse_pos == cat_pos:
            return -1000  
        if turno >= max_turno:
            return 1000
        if mouse_pos == cheese_pos:
            return 1000
    
        dx = abs(mouse_pos[0] - cat_pos[0])
        dy = abs(mouse_pos[1] - cat_pos[1])
        return 5*dx + 2*dy + turno
    
    def minimax(self, profundidad, es_maximizador, cat_pos, mouse_pos, turno, max_turno, tablero, cheese_pos):
        
        if profundidad == 5 or cat_pos == mouse_pos or mouse_pos == cheese_pos or turno + profundidad >= max_turno:
                return self.evaluar_estado(cat_pos, mouse_pos, turno, max_turno, cheese_pos)

        if es_maximizador:
            max_eval = float("-inf")
            
            for move in self.movimientos_validos(tablero, mouse_pos):
                eval = self.minimax(profundidad + 1, False, cat_pos, move, turno, max_turno, tablero, cheese_pos)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            
            for move in self.movimientos_validos(tablero, cat_pos):
                eval = self.minimax(profundidad + 1, True, move, mouse_pos, turno, max_turno, tablero, cheese_pos)
                min_eval = min(min_eval, eval)
            return min_eval
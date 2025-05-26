import random


class Cat:

    # definimos nuestras 4 direcciones posibles
    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
      
    # definimos los ejes, su imagen y una lista vacia para almavenar ultimos movimientos
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.img = "😾"
        self.ultimos_movimientos = []

    # definimos es movimiento valido para que nos retorne true o false
    def es_movimiento_valido(self, tablero, x, y):
        # si esta fuera del tablero
        if not (0 <= x < tablero.filas and 0 <= y < tablero.columnas):
            return False
        # si hay una (X)
        if tablero.tablero[y][x] == '❌':
            return False
        
        return True


    def movimiento_aleatorio (self, tablero):

        # guardamos una variable con las direcciones y las colocamos de forma random
        direcciones = self.DIRECCIONES.copy()
        random.shuffle(direcciones)  

        # recorremos todas las direcciones
        for dx, dy in direcciones:
            nuevo_x = self.ejex + dx
            nuevo_y = self.ejey + dy

            # si es un movimeitno valido, almacenamos como nueva ubicacion y rompemos el for
            if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                self.ejex = nuevo_x
                self.ejey = nuevo_y 
                break 

    def movimiento_usuario (self, tablero):

        # buble infinito para asegurar que se seleccione una direccion
        while True:   
            # una variable para la direccion ingresada y otra para los movimientos validos      
            direccion = input("Ingrese una direccion [W, A, S, D] ").strip().lower()
            movimientos = {
                "w" : (0,-1),
                "s" : (0,1),
                "a" : (-1,0),
                "d" : (1,0)
            }

            # si existe la direccion en movimientos
            if direccion in movimientos:

                # almacenamos ese movimiento en dos variables
                dx, dy = movimientos[direccion]
                nuevo_x = self.ejex + dx
                nuevo_y = self.ejey + dy

                # es es valida, modificamos posicion y rompemos el buble
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y
                    break
                else:
                    print("Movimiento no válido")

            else:
                print("Comando no reconocido, comandos validos [W, A, S, D] ")
    
    # definimos la validacion de movimiento
    def movimientos_validos(self, tablero, pos=None):

        if pos == None:
            pos = (self.ejex, self.ejey) 

        posibles = [] # retornaremos una lista con todos los movimientos que pueda hacer

        # por cada movimiento nos cercioramos que no este fuera del tablero y no haya una (X)
        for dx, dy in self.DIRECCIONES:
            nuevo_x = pos[0] + dx
            nuevo_y = pos[1] + dy
            if 0 <= nuevo_x < tablero.filas and 0 <= nuevo_y < tablero.columnas:
                if tablero.tablero[nuevo_y][nuevo_x] != '❌':
                    posibles.append((nuevo_x, nuevo_y))

        return posibles

    # funcion del movimiento del gato con minimax
    def movimiento_AI (self, mouse_pos, tablero, turno, max_turno, cheese_pos):

        # almacenamos en una variable nuestro mejor movimiento
        mouse_pos = (mouse_pos.ejex, mouse_pos.ejey)
        cheese_pos = (cheese_pos.ejex, cheese_pos.ejey)
        mejor_movimiento = self.get_best_move(mouse_pos, tablero, turno, max_turno, cheese_pos)
        
        # si existe mejor movimiento lo establecemos como nueva posicion del gato
        if mejor_movimiento:
            self.ejex, self.ejey = mejor_movimiento
           
           # agregamos ese movimiento a la lista de ultimos movimientos
            self.ultimos_movimientos.append(mejor_movimiento)
            if len(self.ultimos_movimientos) > 4:
                self.ultimos_movimientos.pop(0)

    # funcion para elejir el mejor movimiento
    def get_best_move(self, mouse_pos, tablero, turno, max_turno, cheese_pos):
        # dos variables de inicio 
        best_score = float("-inf")
        best_move = None

        # por cada movimeinto que haya en movimiento validos
        for move in self.movimientos_validos(tablero):

            #backup de posicion del gato y definimos como nueva ubicacion la ubicacion a probar
            backup_cat_pos = (self.ejex, self.ejey)
            self.ejex, self.ejey = move

            # guardamos el puntaje de ese movimiento
            score = self.minimax(0, True, move, mouse_pos, turno, max_turno, tablero, cheese_pos)

            # penalizamos si es un movimiento repetido
            if len(self.ultimos_movimientos) >= 2: 
                if move in self.ultimos_movimientos:
                 score -= 5 

            # restablecemos la ubicacion del backup
            self.ejex, self.ejey = backup_cat_pos

            # si el puntaje es mejor, ese movimientro es el mejor movimiento
            if score > best_score:
                best_score = score
                best_move = move

        return best_move   
    
    def evaluar_estado(self, cat_pos, mouse_pos, turno, max_turno, cheese_pos):
        # mejor puntaje posible
        if mouse_pos == cat_pos:
            return 100  
        
        # peores puntajes posibles
        if turno >= max_turno:
            return -100
        if mouse_pos == cheese_pos:
            return -100
    
        # almacenamos en variables las distancias
        distancia_ejex = abs(mouse_pos[0] - cat_pos[0])
        distancia_ejey = abs(mouse_pos[1] - cat_pos[1])

        # castigamos mientras mas distancia haya con el raton
        return -(3*distancia_ejex + 2*distancia_ejey + turno)
    
    def minimax(self, profundidad, es_maximizador, cat_pos, mouse_pos, turno, max_turno, tablero, cheese_pos):
        
        # estado de salida, retornamos un puntaje
        if profundidad == 5 or cat_pos == mouse_pos or mouse_pos == cheese_pos or turno + profundidad >= max_turno:
                return self.evaluar_estado(cat_pos, mouse_pos, turno, max_turno, cheese_pos)

        # si es el maximizador (El gato)
        if es_maximizador:
            # iniciamos una variable max
            max_eval = float("-inf")
            
            # por cada movimiento disponible, damos un puntaje y almacenamos si es el mejor puntaje
            for move in self.movimientos_validos(tablero, cat_pos):
                eval = self.minimax(profundidad + 1, False, move, mouse_pos, turno, max_turno, tablero, cheese_pos)
                max_eval = max(max_eval, eval)
            return max_eval
        
        # caso contrario es minimizador (El raton)
        else:
            min_eval = float("inf")
            
            for move in self.movimientos_validos(tablero, mouse_pos):
                eval = self.minimax(profundidad + 1, True, cat_pos, move, turno  + 1, max_turno, tablero, cheese_pos)
                min_eval = min(min_eval, eval)
            return min_eval
    
   


# practicamente igual que el gato
class Mouse:

    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.img = "🐭"
        self.ultimos_movimientos = []
    
    def es_movimiento_valido(self, tablero, x, y):
        if not (0 <= x < tablero.filas and 0 <= y < tablero.columnas):
            return False
        if tablero.tablero[y][x] == '❌':
            return False
        if tablero.tablero[y][x] == '😾': # el no puede moverse donde esta el gato
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
            direccion = input("Ingrese una direccion [W, A, S, D] ").strip().lower()
            movimientos = {
                "w" : (0,-1),
                "s" : (0,1),
                "a" : (-1,0),
                "d" : (1,0)
            }

            if direccion in movimientos:
                dx, dy = movimientos[direccion]
                nuevo_x = self.ejex + dx
                nuevo_y = self.ejey + dy

                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y
                    break
                else:
                    print("Movimiento no válido")

            else:
                print("Comando no reconocido, comandos validos [W, A, S, D] ")


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
            if 0 <= nuevo_x < tablero.filas and 0 <= nuevo_y < tablero.columnas:
                if tablero.tablero[nuevo_y][nuevo_x] != '❌' and tablero.tablero[nuevo_y][nuevo_x] != '😾':
                    posibles.append((nuevo_x, nuevo_y))

        return posibles    

    def get_best_move(self, cat_pos, tablero, turno, max_turno, cheese_pos):
        best_score = float("-inf")
        best_move = None

        for move in self.movimientos_validos(tablero):

            backup_mouse_pos = (self.ejex, self.ejey)
            self.ejex, self.ejey = move

            score = self.minimax(0, True, cat_pos, move, turno, max_turno, tablero, cheese_pos)

            if len(self.ultimos_movimientos) >= 2:
                if move in self.ultimos_movimientos:
                    score -= 5 

            self.ejex, self.ejey = backup_mouse_pos

            if score > best_score:
                best_score = score
                best_move = move

        return best_move   

    def evaluar_estado(self, cat_pos, mouse_pos, cheese_pos):

        ## mejor puntaje posible
        if mouse_pos == cheese_pos:
            return 200

        # guardamos en una variable la distancia que hay con el gato
        gato_ejex = abs(mouse_pos[0] - cat_pos[0])
        gato_ejey = abs(mouse_pos[1] - cat_pos[1])
        distancia_gato = gato_ejex + gato_ejey

        # dependiendo de la distancia castigamos
        if distancia_gato == 0:
            return -200
        elif distancia_gato == 1:
            castigo_gato = -100
        elif distancia_gato == 2 or distancia_gato == 3:
            castigo_gato = -50
        else:
            castigo_gato = 0

        # guardamos en otra variable la distancia con el queso
        queso_ejex = abs(mouse_pos[0] - cheese_pos[0])
        queso_ejey = abs(mouse_pos[1] - cheese_pos[1])
        distancia_queso = queso_ejex + queso_ejey 

        # premiamos si esta super cerca, y castigamos mientras mas lejos este
        if distancia_queso == 1:
            castigo_queso = 150
        else:
            castigo_queso = -(distancia_queso * 10)

        return castigo_gato + castigo_queso


    
    def minimax(self, profundidad, es_maximizador, cat_pos, mouse_pos, turno, max_turno, tablero, cheese_pos):
        
        if profundidad == 5 or cat_pos == mouse_pos or mouse_pos == cheese_pos or turno + profundidad >= max_turno:
                return self.evaluar_estado(cat_pos, mouse_pos, cheese_pos)

        if es_maximizador:
            max_eval = float("-inf")
            
            for move in self.movimientos_validos(tablero, mouse_pos):
                eval = self.minimax(profundidad + 1, False, cat_pos, move, turno, max_turno, tablero, cheese_pos)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            
            for move in self.movimientos_validos(tablero, cat_pos):
                eval = self.minimax(profundidad + 1, True, move, mouse_pos, turno + 1, max_turno, tablero, cheese_pos)
                min_eval = min(min_eval, eval)
            return min_eval
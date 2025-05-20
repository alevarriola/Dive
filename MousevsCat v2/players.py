import random

class Cat:

    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
      
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.ultimos_movimientos = []
    
    def es_movimiento_valido(self, tablero, x, y):
        if not (0 <= x < 10 and 0 <= y < 10):
            return False
        if tablero.tablero[y][x] == '❌':
            return False
        return True

    def movimiento (self, getBest_func):

        mejor_movimiento = getBest_func()
        
        if mejor_movimiento:
            self.ejex, self.ejey = mejor_movimiento

            self.ultimos_movimientos.append(mejor_movimiento)
            if len(self.ultimos_movimientos) > 4:
                self.ultimos_movimientos.pop(0)



class Mouse:

    DIRECCIONES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
    
    def es_movimiento_valido(self, tablero, x, y):
        if not (0 <= x < 10 and 0 <= y < 10):
            return False
        if tablero.tablero[y][x] == '❌':
            return False
        return True

    def movimiento_IA (self, getBest_func):

        mejor_movimiento = getBest_func()
        
        if mejor_movimiento:
            self.ejex, self.ejey = mejor_movimiento
            self.ultimo_movimiento = mejor_movimiento

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
            print(direccion)

            if direccion == "w":
                nuevo_x = self.ejex
                nuevo_y = self.ejey - 1
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    print(f"Ratón se movió a ({self.ejex}, {self.ejey})")
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "s":
                nuevo_x = self.ejex
                nuevo_y = self.ejey + 1
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    print(f"Ratón se movió a ({self.ejex}, {self.ejey})")
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "a":
                nuevo_x = self.ejex - 1
                nuevo_y = self.ejey
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    print(f"Ratón se movió a ({self.ejex}, {self.ejey})")
                    break
                else:
                    print("Movimiento no valido")

            elif direccion == "d":
                nuevo_x = self.ejex + 1
                nuevo_y = self.ejey
                if self.es_movimiento_valido(tablero, nuevo_x, nuevo_y):    
                    self.ejex = nuevo_x
                    self.ejey = nuevo_y 
                    print(f"Ratón se movió a ({self.ejex}, {self.ejey})")
                    break
                else:
                    print("Movimiento no valido")

            else:
                print("Comando no reconocido, comandos validos [W, A, S, D]")



        


class Tablero:
    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self.tablero = [['⬜' for _ in range(self.filas)] for _ in range(self.columnas)]
        
    def print_tablero(self):
        borde = '⬛ ' * (self.columnas + 2)

        print(borde)
        for fila in self.tablero:
            print('⬛ ' + ' '.join(fila) + ' ⬛')
        print(borde)
            

    def reset(self):
        self.tablero = [['⬜' for _ in range(self.filas)] for _ in range(self.columnas)]


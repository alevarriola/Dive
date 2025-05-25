class Tablero:

    # Definimos el init del tablero con filas, columnas y la logica del tablero
    def __init__(self, tamaño):
        self.filas = tamaño
        self.columnas = tamaño
        self.tablero = [['⬜' for _ in range(self.filas)] for _ in range(self.columnas)]
        
    # definimos un print para el tablero, que vera el usuario
    def print_tablero(self):
        borde = '⬛ ' * (self.columnas + 2) # un borde para el tablero (+2 para considerar que hay esquinas)

        print(borde) 
        for fila in self.tablero:
            print('⬛ ' + ' '.join(fila) + ' ⬛') 
        print(borde) 
            
    # Reset a un tablero en blanco
    def reset(self):
        self.tablero = [['⬜' for _ in range(self.filas)] for _ in range(self.columnas)]


class Tablero:
    def __init__(self):
        self.tablero = [['⬜' for _ in range(10)] for _ in range(10)]
        
    def print_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
        print("------------------------------\n")
            

    def reset(self):
        self.tablero = [['⬜' for _ in range(10)] for _ in range(10)]


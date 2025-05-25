# Importamos random para definir ubicacion de los objetos
import random

class Wall:

    #definimos los obstaculos con un ejex, ejey y su imagen
    def __init__(self, tamaño):
        self.ejex = random.randint(0,tamaño-1)
        self.ejey = random.randint(0,tamaño-1)
        self.img = "❌"

class Cheese:

     #definimos el queso con un ejex, ejey que le pasaremos uno random y su imagen
    def __init__(self, ejex, ejey):
        self.ejex = ejex
        self.ejey = ejey
        self.img = "🧀"
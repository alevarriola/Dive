import random

class Wall:

    def __init__(self):
        self.ejex = random.randint(0,9)
        self.ejey = random.randint(0,9)
        self.img = "❌"

class Cheese:

    def __init__(self):
        self.ejex = random.randint(0,9)
        self.ejey = random.randint(0,9)
        self.img = "🧀"
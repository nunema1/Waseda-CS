import random

class Dice:
    def __init__(self, size):
        self.size = size
        self.face = 0
    def roll(self):
        self.face = random.randint(1, self.size)
        return self.face
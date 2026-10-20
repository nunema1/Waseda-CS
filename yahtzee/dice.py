import random

class D6:
    def __init__(self):
        self.size = 6
    def roll(self):
        result = random.randint(1, self.size)
        return result
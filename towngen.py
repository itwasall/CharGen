import random

class Town:
    def __init__(self, name):
        self.name = name
        self.size = self.getSize()
    
    def getSize(self):
        self.sizes = ['Tiny', 'Small', 'Medium', 'Large', 'Massive']
        return random.choice(self.sizes)


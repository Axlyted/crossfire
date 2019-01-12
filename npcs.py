import random

class Human:
    def __init__(self, name="nameless"):
        self.name = name
        self.intellect = random.randint(1, 10)
        self.strength = random.randint(1, 10)
        self.Dextirity = random.randint(1, 10)
        self.HP = random.randint(100, 300)
        self.MP = random.randint(100, 300)
    
    def __str__(self):
        return(
        "name : " + self.name + "\n" +
        "intellect : " + str(self.intellect) + "\n" +
        "strength : " + str(self.strength) + "\n" +
        "Dextirity : " + str(self.Dextirity) + "\n" +
        "HP : " + str(self.HP) + "\n" +
        "MP : " + str(self.MP) + "\n")

class Warrior:
    pass
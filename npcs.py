import random

class Human:
    def __init__(self, name="nameless"):
        self.name = name
        self.lvl = 1
        self.xp = 0

        self.intellect = random.randint(1, 10)
        self.strength = random.randint(1, 10)
        self.Dextirity = random.randint(1, 10)
        self.HP = random.randint(100, 300)
        self.MP = random.randint(100, 300)
    
    def __str__(self):
        return(
        "Name : " + self.name + "\n" +

        "Level : " + str(self.lvl) + "\n" +
        "Experience : " + str(self.xp) + "\n" +

        "Intellect : " + str(self.intellect) + "\n" +
        "Strength : " + str(self.strength) + "\n" +
        "Dextirity : " + str(self.Dextirity) + "\n" +
        "HP : " + str(self.HP) + "\n" +
        "MP : " + str(self.MP) + "\n")

class Warrior(Human):
    def __init__(self):
        pass
    pass
        
    
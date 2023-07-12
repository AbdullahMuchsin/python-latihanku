# BELAJAR OOP PYTHON INHERITANCE

class Hero: # Ini merupakan super class
    def __init__(self,name,health):
        self.name = name
        self.health = health
class Hero_Magic(Hero): # Ini adakah sub class Hero
    pass # Jadi ini bisa mendapatkan varible __init__dari class utama
class Hero_Tank(Hero): # Ini adakah sub class Hero
    pass # Jadi ini bisa mendapatkan varible __init__dari class utama

archer = Hero("Archer", 60)
axe = Hero_Tank("Axe", 90)
gunman = Hero_Magic("GunMan", 75)

print(archer.name)
print(archer.health)

print(axe.name)
print(axe.health)

print(gunman.name)
print(gunman.health)




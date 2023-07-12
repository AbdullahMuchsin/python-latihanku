# BELAJAR PYTHON OOP CLASS AND INSTANCE VARIABLES

class Hero:
    # Class Variables
    jumblah = 0

    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self. health = health 

        print("Ini adalah hero " + self.name)
        Hero.jumblah += 1

print(Hero.jumblah)
hero1 = Hero("Tank", 50, 150)
print(Hero.jumblah)
hero2 = Hero("Mage", 75, 75)
print(Hero.jumblah)
hero3 = Hero("Assasin", 70, 100)
print(Hero.jumblah)



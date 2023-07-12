# BELAJAR OOP MENGGUNAKAN __INIIT__ DALAM CLASS

class Hero:
    def __init__(self, name, power, health, speed, armor): # Self adalah diri sendiri atau object/variable ex. hero1
        print("Ini __init__") # Akan dieksekusi di awal meskipun tidak di print
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed
        self.armor = armor

print("-------------------------------------")
hero1 = Hero("Assasin", 75, 100, 75, 75)
print("-------------------------------------")
hero1 = Hero("Tank", 40, 200, 50, 100)
print("-------------------------------------")
hero1 = Hero("Mage", 75, 100, 50, 40)
print("-------------------------------------")
print(Hero("Assasin", 75, 100, 75, 75).armor) 
print("-------------------------------------")

print(hero1.name)
print(hero1.power)
print(hero1.health)
print(hero1.speed)
print(hero1.armor)


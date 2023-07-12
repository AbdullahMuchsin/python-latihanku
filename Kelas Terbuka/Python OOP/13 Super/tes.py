# BELAJAR OOP PYTHON SUPER

class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.health = health
        self.armor = armor
    def info(self):
        return print("Nama : {}\n\tHealth : {}\n\tArmor : {}".format(self.name,self.health,self.armor))
    
class Hero_Magic(Hero):
    pass

hero = Hero_Magic("name", 100,22)
print(hero.name)
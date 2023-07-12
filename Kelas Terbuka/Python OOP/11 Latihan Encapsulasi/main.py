# BELAJAR OOP PYTHON LATIHAN ENCAPSULASI

class Hero:
    __jumblahHero = 0
    def __init__(self,name,health,attPower,armor,speed):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__speedBase = speed
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level
        self.__speed = self.__speedBase * self.__level

        self.__health = self.__healthMax

        Hero.__jumblahHero += 1

    @property
    def info(self):
        return f"""
Nama         : {self.__name}
Health       : {self.__health}/{self.__healthMax}
Attack Power : {self.__attPower}
Armor        : {self.__armor}
Move Speed   : {self.__speed}       
"""

    @property
    def upExp(self):
        pass

    @upExp.setter
    def upExp(self, addExp):
        self.__exp += addExp
        if (self.__exp) > 100*self.__level:
            print("Level UP !!!")
            self.__level += 1
            self.__exp = 0

            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
            self.__speed = self.__speedBase * self.__level

            self.__health = self.__healthMax
    
    def attack(self, musuh):
        print("Hero " + self.__name + " Menyerang Hero " + musuh.__name)
        musuh.__health -= (self.__attPower // musuh.__armor)
        self.upExp = 50
        self.__attPower += (self.__attPower // musuh.__armor)
        self.__armor += (self.__attPower // musuh.__armor)
        self.__speed += (self.__attPower // musuh.__armor)
        musuh.membela(self)

    def membela(self,musuh):
        print("\nHero " + self.__name + " Diserang oleh Hero " + musuh.__name)
        self.__membela = musuh.__attPower - (self.__attPower//musuh.__armor)
        print("Dari serangan tersebut bisa berthan sebesar : " + str(self.__membela))

sword = Hero("Sword", 100, 10, 15, 5)
archer = Hero("Archer", 100, 20, 10, 10)
print(sword.info)
print(archer.info)

sword.attack(archer)
print(sword.info)
print(archer.info)

archer.attack(sword)
print(sword.info)
print(archer.info)

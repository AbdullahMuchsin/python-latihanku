# Belajar Encapsulasi
'''
    Yaitu Membuat Semua Variable Menjadi Private
    Ada Getter and Setter 
    Getter adalah Mengambil nilai dari Variable yang di private
    Setter adalah Mengubah nilai dari variable yang di private di belakang layar 

'''

class Hero:
    def __init__(self, name, health, powerAttack, armor):
        self.__name = name
        self.__health = health
        self.__powerAttack = powerAttack
        self.__armor = armor

    # Getter
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health
    def getPower(self):
        return self.__powerAttack
    
    # Setter
    def setHealth(self, upHealth):
        self.__health += upHealth
    def setPowerAttack(self):
        self.__powerAttack -= 5

    # Getter and Setter
    def armorUp(self, upArmor):
        self.__armor += upArmor
        return self.__armor
    


GunMan = Hero("GunMan", 100, 15, 20)

# Getter
print(GunMan.getName())
print(GunMan.getHealth())
print(GunMan.getPower())


# Setter
GunMan.setHealth(10)
GunMan.setPowerAttack()
print(GunMan.getHealth())
print(GunMan.getPower())

# Getter and Setter
print(GunMan.armorUp(15))
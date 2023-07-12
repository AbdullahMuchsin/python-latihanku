# BELAJAR OOP PYTHON OVERRIDE METHOD

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def info(self):
        print("Ini dari class Hero")
        print("Nama {}:\n\tHealth {}".format(
            self.name,
            self.health
            )
        )
    
class Hero_magic(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    def info(self): # Kalau ini menimpa nama fungsi dari class utama
        print("Ini dari subclass Hero_ magic") # Membuat struktur sama dengan class utama tapi tidak import
        print("Nama {}:\n\tHealth {}".format(
            self.name,
            self.health
            )
        )       

class Hero_tank(Hero):
    def __init__(self,name):
        super().__init__(name,200)
    def info(self):
        super().info() # Kalau ini ambil dari class utama / import
        
mage = Hero_magic("Mage")
tank = Hero_tank("Tank")

mage.info()
tank.info()
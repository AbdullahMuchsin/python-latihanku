# BELAJAR OOP PYTHON SUPER

class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.health = health
        self.armor = armor
    def info(self):
        return print("Nama : {}\n\tHealth : {}\n\tArmor : {}".format(self.name,self.health,self.armor))
    
class Hero_Magic(Hero):
    # Init utama tidak menerima argumen selain string
    def __init__(self,name): # Perilaku argumen nya sama dengan super class/class utama
        # pakai __init__ turunan untuk argumen angka dll
        Hero.__init__(self,name,100,50) # Selain pakai manggil dengan class utama bisa pakai super() sehingga tidak perlu pakai self
        super().info()

class Hero_Tank(Hero):
    def __init__(self,name):
        super().__init__(name,200,30) # Seper ini contoh pakai super
        Hero.info(self)

archer = Hero_Magic("Archer")
axe = Hero_Tank("Axe")




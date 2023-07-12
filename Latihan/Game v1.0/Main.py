import os
from abc import ABC,abstractmethod
class Hero(ABC):
    def __init__(self,name,health,attPower):
        self.name = name
        self.level = 1
        self.expBase = 100
        self.healthBase = health
        self.attPowerBase = attPower

        self.exp = self.expBase * self.level
        self.health = self.healthBase * self.level
        self.attPower = self.attPowerBase * self.level

    @abstractmethod
    def beat(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    def info(self):
        print(f"""{self.name} :
    Level        : {self.level}
    Experience   : {self.expBase}/{self.exp}
    Health       : {self.health}
    Attack Power : {self.attPower}""")

class Tank(Hero):
    def __init__(self,name,health,attpower):
        super().__init__(name,health,attpower)
        self.__skillBase = 50

    def skillBase(self):
        if self.health < 50:
            self.attPower += self.__skillBase

    def beat(self,enemy):
        print(f"Anda Sedang Menyerang Hero {enemy.name}")
        self.skillBase()
        enemy.health -= self.attPower
        print(f"Anda Berhasil Melukai Lawan Sebesar {self.attPower}")
        enemy.skillBase()
        enemy.defend(self)

    def defend(self,enemy):
        enemy.attdefend = (enemy.attPower//2)
        self.health -= enemy.attdefend
        print(f"Anda Terkena Serangan Balik Sebesar {enemy.attdefend}")
        print("Info Masing-Masing")
        self.info()
        enemy.info()

class Mage(Hero):
    def __init__(self,name,health,attpower):
        super().__init__(name,health,attpower)
        self.__skillBase = 15

    def skillBase(self):
            self.attPower += self.__skillBase

    def beat(self,enemy):
        print(f"Anda Sedang Menyerang Hero {enemy.name}")
        self.skillBase()
        self.health -= self.attPower
        print(f"Anda Berhasil Melukai Lawan Sebesar {self.attPower}")
        enemy.skillBase()
        enemy.defend(self)

    def defend(self,enemy):
        enemy.attdefend = (enemy.attPower//2)
        self.health -= enemy.attdefend
        print(f"Anda Terkena Serangan Balik Sebesar {enemy.attdefend}")
        print("Info Masing-Masing")
        self.info()
        enemy.info()
        
    def infoSkill(self):
        print("Skill DAMAGE ATTACK  : Dengan Menggunakan Hero Mage Setiap Menyerang Akan Selalu Up Power Attack +15")
    
    def info(self):
        super().info()
        self.infoSkill()

def main():
    while True:
        print("1.Banteng")
        print("2.Kupu-Kupu")
        try:
            isSelect = int(input("Pilih Hero : "))
        except:
            print("Hanya Masukan Angka !!!")
        
        if isSelect == 1 or isSelect == "1":
            Bantang.info()
        elif isSelect == 2 or isSelect == "2":
            Butterfly.info()
        else:
            print("Maaf input anda error")

        if isSelect == 1:
            print("Serang Hero !")
            print("1.Banteng")
            print("2.Kupu-Kupu")
            try:
                isBeat = int(input("Pilih Hero yang akan di lawan ? "))
            except:
                print("Hanya Masukan Angka !!!")

            if isBeat == 1 or isBeat == "1":
                Bantang.beat(Bantang)
            elif isBeat == 2 or isBeat == "2":
                Bantang.beat(Butterfly)
                
        if isSelect == 2:
            print("Serang Hero !")
            print("1.Kupu-Kupu")
            print("2.Banteng")
            try:
                isBeat = int(input("Pilih Hero yang akan di lawan ? "))
            except:
                print("Hanya Masukan Angka !!!")

            if isBeat == 1 or isBeat == "1":
                Butterfly.beat(Butterfly)
            elif isBeat == 2 or isBeat == "2":
                Butterfly.beat(Bantang)

        isOption = input("Apakah Mau lanjut (y/n) ? ")
        if isOption == "n" or isOption == "N":
            break
        
Bantang = Tank("Banteng",100,15)
Butterfly = Tank("Kupu-Kupu",75,5)

isRun = True
while isRun:
    os.system("cls")
    main()
    isOption = input("Apakah Mau lanjut (y/n) ? ")
    if isOption == "n" or isOption == "N":
        break



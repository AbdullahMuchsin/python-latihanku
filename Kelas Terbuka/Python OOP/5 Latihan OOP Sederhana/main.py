# LATIHAN SEDERHANA OOP PYHTON MEMBUAT GAME SEDERHANA
import os

class Hero:
    def __init__(self, name, health, powerAttack, armor):
        self.name = name
        self.health = health
        self.powerAttack = powerAttack
        self.armor = armor
    
    def serang(self, lawan):
        print(self.name + " Menyerang " + lawan.name)
        lawan.diserang(self)

    def diserang(self, lawan):
        print(self.name + " Diserang oleh " + lawan.name)
        self.minHealt(lawan)
        print("darah " + self.name + " tinggal : " + str(self.health)) 

    def minHealt(self, lawan):
        minhealth = lawan.powerAttack/self.armor
        self.health -= minhealth
    
    def view(self):
        print(f'''DATA HERO :
Nama   : {self.name}
Health : {self.health}
power  : {self.powerAttack}
Armor  : {self.armor}
        ''')



archer = Hero("Archer", 75, 15, 20)
gun = Hero("GunMan", 100, 30, 5)

print("GAME ATTACK")
print("===========")

print(f"""1. Main
2. Exit
""")

isSelect = int(input("Pilih nomor : "))

os.system("cls")
print("GAME ATTACK")
print("===========")

print("Pilih Karakter :")
print("1. Archer")
print("2. GunMan")

isPilih = int(input("Pilih nomor : "))

while isSelect == 1:
    while isPilih == 1:
        print("GAME ATTACK")
        print("===========")
        archer.view()
        inp = input("Serang " + gun.name + " yes or no ?")
        if inp == "yes":
            archer.serang(gun)
        if inp == "no":
            break
    while isPilih == 2:
        os.system("cls")
        print("GAME ATTACK")
        print("===========")
        gun.view()
        inp = input("Serang " + archer.name + " yes or no ?")
        if inp == "yes":
            gun.serang(gun)
        if inp == "no":
            break
    break

print("Program berakhir")


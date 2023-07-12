'''
    Instance class adalah Object yang di inisialisasi dengan class
    Instance Variable adalah Variable yang di inisialisasi dengan parameter contructor

        class Varibale adalah variable yang dapat berubah dan diakses oleh semua object dan fungsi yang terkait
    dengan class
        Instance Variable or class adalah variable yang hanya dapat di akses dan dirubah oleh
    object yang bersangkutan tanpa terhubung dengan object lain
'''

class Hero:
    jumblah = 0 # Jumblah adalah class variable
    def __init__(self,name,health,attpower):
        self.name = name # Dari baris 14:16 adalah instance varibale
        self.health = health
        self.attpower = attpower

        Hero.jumblah += 1
    
print(Hero.jumblah)
tank = Hero("Banteng",100,15) # object tank dan archer adalah instance class
print(Hero.jumblah)
archer = Hero("GunMan",85,25)
print(Hero.jumblah) # Dapat dilihat varible dari class dapat berubah dari pengaruh object lain




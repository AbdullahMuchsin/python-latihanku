# Rumus - Rumus Matematika
from abc import ABC
class Part(ABC):
    phi = (22/7)
    def __init__(self, panjang, lebar, jari, diameter, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.jari = jari
        self.diameter = diameter
        self.tinggi = tinggi
    
    def info(self):
        print("Info data yang anda berikan :")
        print("Panjang      : " + self.panjang)
        print("Lebar        : " + self.lebar)
        print("Jari - Jari  : " + self.jari)
        print("Diameter     : " + self.diameter)
        print("Tinggi       : " + self.tinggi)

class BangunRuang(Part):
    def __init__(self, panjang = None, lebar = None, jari = None, diameter = None, tinggi = None):
        super().__init__(panjang, lebar, jari, diameter, tinggi)
    def Balok(self):
        # Keliling balok
        kll = 4 * (self.panjang + self.lebar + self.tinggi)
        print("Keliling Balok  : " + str(kll))
        # Luas balok
        luas = 2 * ((self.panjang * self.lebar) + (self.panjang * self.tinggi) + (self.tinggi * self.lebar))
        print("Keliling Luas   : " + str(luas))


        
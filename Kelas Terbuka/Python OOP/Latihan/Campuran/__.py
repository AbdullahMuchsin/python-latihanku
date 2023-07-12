from abc import ABCMeta, abstractmethod

class bangunRuang(metaclass=ABCMeta):
    @abstractmethod
    def get_luas(self):
        "Luas bangun ruang"
    @abstractmethod
    def get_volume(self):
        "Volume bangun ruang"
    def __str__(self):
        return "Hasil dari volume " + str(self.get_volume()) + " dan laus " + str(self.get_luas())

class Balok(bangunRuang):
    def __init__(self,panjang,lebar,tinggi):
        self.__panjang = panjang
        self.__lebar = lebar
        self.__tinggi = tinggi

    def get_luas(self):
        pl = self.__panjang * self.__lebar
        pt = self.__panjang * self.__tinggi
        lt = self.__lebar * self.__tinggi
        return 2 * (pl + pt + lt)
        
    def get_volume(self):
        return self.__panjang * self.__lebar * self.__tinggi
    
def main():
    bangun1 = Balok(2,3,4)
    print(str(bangun1))

main()
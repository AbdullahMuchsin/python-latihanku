
class Hero:
    __jumblah = 0
    def __init__(self,nama, nyawa, kekuatan):
        self.__nama = nama
        self.__nyawa = nyawa
        self.__kekuatan = kekuatan
        Hero.__jumblah += 1
        
    @property
    def nama(self):
        pass
    @property
    def nyawa(self):
        pass
    @property
    def kekuatan(self):
        pass

    @kekuatan.getter
    def kekuatan(self):
        return self.__kekuatan
    @kekuatan.setter
    def kekuatan(self, nambah=0):
        self.__kekuatan += nambah
    @kekuatan.deleter
    def kekuatan(self):
        print("Kekuatan di hapus")
        self.__kekuatan = None
    @nyawa.getter
    def nyawa(self):
        return self.__nyawa
    @nyawa.setter
    def nyawa(self, nambah):
        self.__nyawa += nambah
    @nyawa.deleter
    def nyawa(self):
        print("Nyawa di hapus")
        self.__nyawa = None
    # Classmethods
    @classmethod # Jika di tambah classmethod maka akan bisa di akses oleh class nya tanpa inisialisasi
    def info_jumblah(cls):
        return cls.__jumblah
    @staticmethod # Jika di tambah staticmethod maka akan bisa di akses oleh class yang di inisialisasi juga (data) bukan class (Hero saja)
    def rubah_jumblah(manipulasi):
        __jumblah = manipulasi
        return __jumblah

data = Hero("Muchsin", 100, 100)
data.nyawa = 50
print(data.nyawa)
del data.kekuatan
print(data.kekuatan)
print(data.__dict__)
print(Hero.info_jumblah())
print(data.rubah_jumblah(20))
print(data.rubah_jumblah(20))
# Optional parameters sama hal nya dengan parameter dafault
# example
def func(x=5 ,y=1):
    hasil = 25 * (x + y)
    return hasil

func_1 = func()
print(func_1)

print("=====================================")
class Toko:
    def __init__(self, nama:str, jenis:str="Sembako",jam_kerja:float=None):
        self.nama = nama
        self.jenis = jenis
        self.jam_kerja = jam_kerja
    
    def info(self, isOpen:bool=True):
        if isOpen:
            print("TOKO :",self.nama.upper())
            print("Jenis Toko :",self.jenis)
            print("Buka Mulai Jam :",self.jam_kerja)
        else:
            print("Maaf info ini sedang di encapsulasi")

toko1 = Toko(nama="REZEKI",jam_kerja=17.00)
toko1.info()
print("=====================================")
toko1.info(False)
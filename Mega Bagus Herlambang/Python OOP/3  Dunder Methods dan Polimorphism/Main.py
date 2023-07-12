# Polimorphism
# Polimorphism adalah atribut or parameter dari fungsi lain yang memilki sifat dan atribut dari class

class Motor:
    def __init__(self,brand, size):
        self.brand = brand
        self.size = size
    
    def info(self):
        print("Nama   : " + self.brand)
        print("Ukuran :", self.size)
    
class Mobil:
    def __init__(self,brand, size):
        self.brand = brand
        self.size = size
    def info(self):
        print("Nama   : " + self.brand)
        print("Ukuran :", self.size)

suzuki = Motor("Suzuki",200)
toyota = Mobil("Toyota",600)

# Misal pake for 
print("============= FOR")
for jenis in [suzuki,toyota]:
    jenis.info()
    print("")

# Atau Pakai Fungsi
def infoDetail(motor,mobil):
    print("============== FUNCTION")
    motor.info()
    print("")
    mobil.info()

# Main
infoDetail(suzuki, toyota)

# Magic Methods / Dunder
# Yaitu Mehods yang nama nya di awali 2 __ dan di akhiri 2 __ ex. __init__

class Toko:
    def __init__(self, nama, jenis, buka):
        self.nama = nama
        self.jenis = jenis
        self.buka = buka
    def __str__(self):
        return self.nama
    def __len__(self):
        return self.buka

print("=================== DUNDER")
jaya = Toko("Toko Jaya","Sembako",5)
print(jaya.buka)
print(dir(jaya))
print(jaya.__str__())
# print(len(jaya)) # Akan Error
# Karena len itu tipe datanya integer jadi harus sama
print(jaya.__len__()) # Tapi jika manggil dengan cara seperti ini tidak akan error

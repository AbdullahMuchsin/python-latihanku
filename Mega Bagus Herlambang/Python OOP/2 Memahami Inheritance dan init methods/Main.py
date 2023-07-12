# Belajar init method
class Penjual:
    stok = 5 # Ini disebut atribut golobal atribut yang dapat digunakan oleh semua fungsi milik classnya
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.diskon = "50%"
    def Keterangan(self, status = None):
        print(f"Barang {self.brand} Dengan Harga {self.price} dan Memilki Stok {self.stok} Status Barang {status} dan Memilik diskon sebesar {self.diskon}")
tv = Penjual("LG", 500)
tv.Keterangan(status="Bekas")

# Latihan Mencoba Membuat Rumus Balok
class Lingkaran:
    phi = 3.14
    def __init__(self,radian):
        self.radian = radian
        self.luas = self.phi * (radian ** 2)
    def Keliling(self):
        return 2 * self.phi * self.radian

li = Lingkaran(10)
print(li.luas)
print(li.Keliling())

# Belajar Inheritance
# Inheritance adalah pewarisan dimana class anak dapat mewarisi atribut dan fungsi dari class induk

# Example
class Transportasi:
    status = None

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def Keterangan(self):
        print(f"Nama {self.nama} Kelas {self.kelas} Status Sebagai {self.status}")

class Nilai(Transportasi):

    def __init__(self, name, kelas):
        super().__init__(name,kelas)
        self.nilai = []
        self.hasil = None

    def tambah(self, tambah):
        self.nilai.append(tambah)

    def mean(self):
        self.mean = 0
        for i in self.nilai:
            self.mean += i
        self.hasil = self.mean / len(self.nilai)
        print("Hasil Rata-rata Nilai nya adalah : " + str(self.hasil))
    def roling(self,rol):
        self.status = rol

muchsin = Nilai("Muchsin",12)

print(muchsin.hasil)
muchsin.Keterangan()
muchsin.tambah(90)
muchsin.tambah(95)
muchsin.tambah(96)
muchsin.tambah(98)
muchsin.mean()
print(muchsin.nilai)
print(muchsin.hasil)
print(muchsin.status)
muchsin.roling("Siswa")
print(muchsin.status)
muchsin.Keterangan()
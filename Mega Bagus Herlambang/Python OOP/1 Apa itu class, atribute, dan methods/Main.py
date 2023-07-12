# EXAMPLE

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

barang1 = Laptop(brand="Redmi",price=1700)
print(type(barang1))
barang1.brand
print(barang1.price)

# class Laptop harus ada isi nya jika tidak ada tambahkan pass agar saat di jalankan tidak error
# class Laptop di atas ada fungsi __init__ yaitu fungsi pertama kali di jalankan saat suatu
# Variable di definisika pada class dan di fungsi init ada nama nya argumen atau parameter
# Di dalamnya dan saat variable di inisialisasikan pada class makan parameter tersebut harus di isi
# Tapi untuk parameter self tidak usah karena self itu mempresentasika class Kulkas itu ke dalam variable
# Yang di inisialisasikan pada class.
# kenapa di dalam fungsi __init__ ada self.brand / atribute di situ lala di inisialisasi dengan parameter
# fungsi __init__? itu sama halnya membuat variable/atribute biasa tapi ditambah self agar yang dapat
# Memanggil hanya variable yang di inisialisasika pada class atau class itu sendiri
# sehingga nama parameter dan atribute dapat sama ataupun berbeda
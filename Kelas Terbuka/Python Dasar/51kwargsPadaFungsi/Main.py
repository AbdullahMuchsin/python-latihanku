# BELAJAR **KWARGS FUNGSI
import math
def luas_segitiga(nama,alas,tinggi):
    print(f"Menghitung {nama}")
    hasil = (1/2 * alas * tinggi)
    return hasil

HASIL = luas_segitiga("Luas Segitiga",24,4)
print(HASIL)

# Menggunkan **kwargs args yaitu sama kayak dictionary ada key nya and value
def data_diri(**data):
    nama = data["nama"]
    umur = data["umur"]
    kota = data["kota"]
    status = data["status"]
    darah = data["darah"]

    print(f"""
    Nama   : {nama}
    umur   : {umur}
    kota   : {kota}
    status : {status}
    darah  : {darah}
    """)
data_diri(nama = "Surudin", umur = 19, kota = "Yogyakarta", status = "Belum Menika", darah = "O")

# Menggunkan **kwargs and *args fungsi
def aritmatika(*data,**option):
    print("ARITMATIKA".center(40,"="))
    hasil = False
    if option["pilihan"] == "eksponen":
        hasil = 2
        for data in data:
            hasil **= data
    elif option["pilihan"] == "pembagian":
        hasil = 100
        for data in data:
            hasil /= data
    else:
        print("Keyword anda :")
    return hasil
HASLIL = aritmatika(2,2,2,2,2,2,2, pilihan = "pembagian")
print(HASLIL)

HASLIL = aritmatika(2,2,2,2,2,2,2, pilihan = "salah")
print(HASLIL)

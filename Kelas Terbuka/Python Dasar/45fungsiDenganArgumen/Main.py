## BELAJAR FUNGSI DENGAN ARGUMEN
import math
from copy import deepcopy

def volume_tabung(jari_jari,tinggi):
    panjang = len("Menghitung Volume Tabung")
    print("\n" + "-"*panjang)
    print("Menghitung Volume Tabung")
    print("-"*panjang + "\n")
    hasil = (math.pi * (jari_jari**2) * tinggi)
    print(f"Volume tabung tersebut adalah : {hasil:.2f}")
    print("="*panjang)


volume_tabung(2,10)

def nama_buah(koleksi_buah):
    panjang = len("Nama-Nama Buah")
    print("\n" + "-"*panjang)
    print("Nama-Nama Buah")
    print("-"*panjang + "\n")
    copy_buah = deepcopy(koleksi_buah)

    for nama in copy_buah:
        print(f"Ada Buah {nama}")
    
    print("="*panjang)


buah = ["Apel","anggur","Melon","Nanas"]
nama_buah(buah)
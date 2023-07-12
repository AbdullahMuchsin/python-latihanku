import Struktur
import os

dataKontak = {}
isRun = True

while isRun:
    os.system("cls")

    print("-"*20)
    print(f"{'DAFTAR KONTAK':^20}")
    print("-"*20)

    print("""
1. Melihat daftar kontak
2. Menambahkan Kotak
3. Menghapus Kontak
4. Cari Kontak
5. Akhir Program
    """)
    isSelect = int(input("Masukan Nomor Yang Anda Pilih : "))

    if isSelect == 1:
        if  bool(dataKontak) == True:
            Struktur.lihat(dataKontak)
        else:
            print("Data Belum ada !!!")
    elif isSelect == 2:
        Struktur.tambah(dataKontak)
    elif isSelect == 3:
        if  bool(dataKontak) == True:
            Struktur.kunci(dataKontak)
            key = input("Masukan KEY Kontak Yang Ingin Dihapus : ")
            Struktur.hapus(dataKontak,key)
        else:
            print("Data Belum ada !!!")
    elif isSelect == 4:
        if  bool(dataKontak) == True:
            key = input("Masukan KEY Kontak Yang Ingin Anda Cari : ")
            Struktur.cari(key,dataKontak)
        else:
            print("Data Tidak Ditemukan !!!")
    elif isSelect == 5:
        break
    else:
        print("Nomor Yang anda Masukan Tidak Ada !!!")

    isOption = input("Apakah anda mau lanjut (y/n) : ")
    if isOption == 'n':
        break

print("\n","AKHIR DARI PROGRAM".center(20,"="))
    

    
